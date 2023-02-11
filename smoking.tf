terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>3.3.0"
    }
  }
}


provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0735c191cf914754d"
  instance_type = "t2.micro"

  user_data = <<-EOF
#!/bin/bash

# Update the system
sudo apt-get update

# Install mini conda and initiate the base environment
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
conda init

# Clone the git repository
git clone https://github.com/sivachandanc/SmokerStatusPrediction.git
cd SmokerStatusPrediction

# Create the logs folder
mkdir logs

# Create the Python 3.7 environment
conda create --name smoke python=3.7

# Activate the smoke environment
conda activate smoke

# Install packages from the requirements.txt file
pip install -r requirements.txt

# Open a tmux session and activate the smoke environment
tmux new-session -s smoke_env -d
tmux send-keys -t smoke_env "conda activate smoke" Enter

# Run the streamlit app
tmux send-keys -t smoke_env "streamlit run streamlit_app.py" Enter
EOF

  tags = {
    Name = "smoking_instance"
  }

  vpc_security_group_ids = [aws_security_group.smoking_security.id]
  iam_instance_profile = aws_iam_instance_profile.smoking_role.name
}

resource "aws_security_group" "smoking_security" {
  name        = "smoking_security"
  description = "Allow HTTP and HTTPS traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_iam_role" "smoking_role" {
  name = "smoking_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_instance_profile" "smoking_role" {
  name = "smoking_role"
  role = aws_iam_role.smoking_role.name
}

resource "aws_iam_policy" "smoking_policy" {
  name = "smoking_policy"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "ssm:*",
        Effect = "Allow",
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "smoking_role_attachment" {
  policy_arn = aws_iam_policy.smoking_policy.arn
  role       = aws_iam_role.smoking_role.name
}
