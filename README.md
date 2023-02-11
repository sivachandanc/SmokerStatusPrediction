
# Smoke Status Prdeiction

This a small project inovolving small scale Data Enginnering and Data Science. This project involves creating a webapp which given the parameters will detect wether the pateint Smokes or Not

## OS
This project is primarily designed for Linux systems.
## Snowflake 
Before going further into project first create a free Snowflake account and make a note of

* username
* password
* [account_identifier](https://sivachandanc.medium.com/ingesting-local-files-to-snowflake-table-using-snowsql-396301578fde#:~:text=The%20tricky%20part,account_locator%20is%20%E2%80%9Ctdb1209%E2%80%9D.)
## AWS CLI
Follow the medium article to install and configure AWS CLI
* [Medium Article](https://medium.com/@greg.farrow1/quick-start-guide-aws-cli-53254f84130)

**Caution:**
Make sure while configuring aws cli put the region as **us-west-2**
## Requirements
The following software and tools are required for this project:
- [AnacondaDistribution](https://www.anaconda.com/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- AWS EC2
- AWS System Manager's Parameter store 
- Snowflake

## Data Source
I have obtained this data from Kaggle.
- [Data](https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction)

## Deploying the project Locally

**Note:**
Assuming your are using linux based system and has installed Anaconda distribution and configured aws cli

1. Cloning the repo

```
git clone https://github.com/sivachandanc/SmokerStatusPrediction

```
```
cd SmokerStatusPrediction

```
2. Creating a Python 3.7 Envirnomnet using Conda

```
conda create -n my_env python=3.7

```
3. Activating the Virtual Env

```
conda activate my_env

```
4. Installing python dependencies

```
pip install -r requirements.txt

```
5. Storing the snowflake credentials in Parameter store

```
python parameters.py -u <user_name> -p <pasword> -a <account_identifier>

```
**Note:**
If your password has special characters use **""**

6. Ingesting data into snowflake

```
python first_load.py -d "<database>" -t "<table>" -s "<schema>" -fp "<data_path>"

```
7. Training the model
```
python model.py

```
8. Running the streamlit web app
```
streamlit run streamlit_app.py

```







## 🚀 About Me

I am a highly motivated data engineer with 4 years of experience in designing, building and maintaining data pipelines. I have a passion for creating efficient and scalable solutions for managing and analyzing large amounts of data. My expertise includes working with various data storage systems, data integration techniques, and big data technologies such as Hadoop and Spark. I am also well-versed in programming languages such as Python and SQL. With my technical skills and attention to detail, I am confident in delivering high-quality data solutions to meet the needs of my clients.



## 🔗 Links
[![Medium](https://img.shields.io/badge/medium-medium-black)](https://sivachandanc.medium.com)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siva-chandan-chakka/)

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Support

For support, email sivachandan1996@gmail.com
