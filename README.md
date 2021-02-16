# Capstone Project: Green Bonds

## Copyright Notice

> Impact-Green-Capstone repository is for the open-source data visualization platform, [Impact Green](https://impact-green.herokuapp.com/), for green bond municipal issuers to track the impact of their green bond infrastructure projects. 
Copyright (C) 2020, Capstone Team (Yueshan Lin, Yiran Pan, Chizobam Nwagwu, Tristan Pang, Yiting Hui, and Xuanming Cao) and Summer PIL Fellows (Sharleen Devjani, Sanika Sahasrabuddhe, and Sarah Sherwood).  

> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

> Read the full terms and conditions of the license [here](https://github.com/impact-green/Impact-Green-Capstone/blob/master/LICENSE.md)

## Getting Started:

> Impact Green made with [Material UI's](https://material-ui.com) components, [React](https://reactjs.org) and Django.

## Vesions and Cloud Deployment
To see codes before cloud deployment, please go to git commit history: [ed04c14](https://github.com/yiran123/Capstone/tree/ed04c14b02edffe26ca7292064dda1fdf8fafafa)

To see codes after cloud deployment, please go to git commit history: [31f03c7](https://github.com/yiran123/Capstone/tree/31f03c721596a2ec3e2fed8caf07c42119292f3e) (Latest commit)

To run and debug the program locally, it is suggested to download the commit version before deployment [ed04c14](https://github.com/yiran123/Capstone/tree/ed04c14b02edffe26ca7292064dda1fdf8fafafa). However, it is worth noting that some modifications are made to the program after cloud deployment. Thus, you may find discrepancies between the two commits mentioned above.

For cloud deployment guide, please refer to this [file](https://drive.google.com/drive/folders/10qkFwZWNBpwQbLCZCy9VYbCjqwbOJEHr?usp=sharing).

## Runtime:

-   Nodejs 10.15.3 or up

-   npm 6.14.8 or up

-   Python 3.8.5 or up

## Web Framework

-   Reactjs version 16.13.1

-   Django version 3.1.1

## Packages Installation:

Create Python virtual environment for package management.

`pip install virtualenv`

`python3 -m venv env`

And install all backend packages:

`pip3 install -r requirements.txt`

Frontend packages are referred in [package.json file](./package.json). When you run the following command, the frontend packages will be installed automatically.

`npm install`

## Running
-   Frontend
    cd frontend/sdg-project
    `npm install`

    Run UI frontend locally:
    `npm start`

    View on
    `localhost:3000`

-   Backend
    `python3 manage.py runserver`

## Documentation

The documentation for the React Material Kit is can be found [here](https://material-ui.com).

## System Structure
The backend and the frontend communicate through [Django-Rest API's](https://www.django-rest-framework.org/). You may also refer to [serializers.py](./greenBondApp/api/serializers.py) for more details.

Fo the issuers' signin, Django-rest-auth is used for backend. You may refer to this [document](https://django-rest-auth.readthedocs.io/en/latest/) for more detail.

## Excel Template
The uploader of this program requires the issuers to upload an excel file to our website, so that our website writes data to the database. To see the template, you may refer to this [example](https://docs.google.com/spreadsheets/d/1J1pcknSblta2Eob8xePS4_3MA3r2lvUP/edit#gid=952669077).

## TODO List:

-   Differente environmental impact data for different project type.

There are three types of projects: water, power and waste water. Different types of projects may have different environmental impact data:

* Power
    * Capacity of Renewable Energy Plant Constructed or Rehabilitated 
    * Capacity of Renewable Energy plants to be Served by Transmission Systems
    * Gross GHG emissions from the Project (CO2e)
    * Energy Savings (J)
* Water
    * Water Reduction (Tons)
    * Water Catchment
* Wastewater
    * Gross Amount of Water (Treated) - Before
    * Gross Amount of Water (Reused)- Before
    * Gross Amount of Water (Avoided) - Before
    * Gross Amount of Water (Treated) - After
    * Gross Amount of Water (Reused)- After
    * Gross Amount of Water (Avoided) - After
    * Energy generation from non-recyclable waste in energy-efficient waste-to-energy facilities (J)
    * Energy recovered from waste (minus any support fuel) (J)
    * Gross amount of waste that is separated and/or collected and treated (including composted) or disposed of (kg)

You may consider model inheritance in Django. Please refer to this [document](https://docs.djangoproject.com/en/3.1/topics/db/models/#model-inheritance).

-   Issuers signup

Note that issuers data has not been created in our Github repository due to the limited time. You may  want to design an authorization method for issuer registration. That is to say, not everyone could signup as an issuer in our website, since the issuers could add/edit/delete data in our database. We want that only the authorized person can manage the data in our database.

One of the solutions for issuer registration is as follows. When the potential issuer signup in our website, an email will be sent to a central admin person. This admin person could approve this signup application or reject it. However, more user research should be conducted about how the central admin person could judge on the issuer applicant's qualification, and decide to approve or reject the application.

Django-rest-auth package supports user registeration. You may refer to this [document](https://django-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional).

-   Bond ratings data

Investors may be interested in bond ratings. You may add bond ratings to bond model. Also, the excel sheet template and uploader should be changed accordingly.

-   Editing/deleting data
The current version only supports writing data into the database using an Excel file. It is strongly recommended that editing and deleting operations be provided.

For adding data to the database, the users are supposed to upload Excel files to our website; then our website writes the data in the database for the user. For editing and deleting data in the database, however, we recommend that an UI should be provided to the user to edit and delete the data.

Users may want to display all or some of the data in the UI, along the buttons for editing and deleting the data. Note that the users may not necessarily find the data they want to edit/delete easily. Therefore, it is also recommended that you provide a searching function for this editing/deleting UI. This program already provides a filtering function in bond page. You can select SDG tags, or issue year to search for a particular bond. However, in next phase, it is recommended that you also provide searching tools for project data, financial data and environmental impact data.

-   Restrict Accesses to APIs

Some APIs should be limited to only authorized users, i.e. issuers. When the users enter the uploader URL without loging in, the program should be directed to other page. You may refer to this [post](https://stackoverflow.com/questions/31084779/how-to-restrict-access-to-routes-in-react-router) for more details restricting API accesses.
