# Automate Fetching and uploading data to Kaggle

These bunch of files deal with the procurement of data for Covid-19 Vaccinations in India, preprocessing them according to the requirements and uploading them to Kaggle datasets.

This project is aimed to automate the process of updating the data every day. The data gets updated each day and so automating the whole process would eliminate the repetitive task.

## Data Source

The data is fetched from Government of India Website and OWID(Our World in Data) github repo.
- [OWID Github repo](https://github.com/owid/covid-19-data)
- [Ministry of Health and Family Welfare - Government of India](https://www.mohfw.gov.in/)

The OWID repo contains data about the daily vaccinations. The Mohfw website is used to get the statewise data.

## Technologies Used

- [wget](https://www.gnu.org/software/wget/) - GNU Wget is a computer program that retrieves content from web servers.
- [Kaggle API](https://www.kaggle.com/docs/api#interacting-with-datasets) - To upload dataset to Kaggle through the API commands.

```wget``` should be downloaded and set according to the procedure on its website. A ```Kaggle API key``` is required in order to use the API.

## Setting Virtual Env for Data Processing Files

Install virtual environment package:

```pip install virtualenv```

Setting a virtual environment:
- Inside the ML_Pipeline folder

```python3 -m venv env-name```

Activating env:

```env-name\Scripts\activate.bat```

Install the required packages:

```pip install -r requirements.txt```

## Execution of the pipeline

Run the ```execute_pipeline.bat``` file which will run the batch files for fetching the data(i.e. ```fetch.bat``` & ```fetch2.bat```) and also that for uploading the data on Kaggle(i.e. ```upload_data.bat```)

This will run the command prompt for running the batch files fetching the data, storing it in ```Raw Data``` folder. Then processing the data in proper format and store it in ```Processed Data``` folder. These files will finally be uploaded to Kaggle using API.

This is a very specific project for my requirements and dataset. It just gibes an idea about how you can implement similar procedure for your datasets, for uploading them to kaggle.

## Automate this process

- Uploading the dataset every day after it is updated can be a tedious task. A task can be scheduled on your machine to execute the pipeline eevery day at a specific time. Thus reducing the intervention needed to upload every time and keep the data up-to-date.

## Licence 

- Licensed under [MIT License](LICENSE.md)