# Internet Services Management Platform
This is a simple CRM project for providing ISP services.
![InternetServicesManagementPlatform  drawio](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/e55d786d-98d8-472d-8559-46f8d8173b58)

### Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata load.json`

### After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin`
  - Password: `1qazcde3`
  - 
## Features

* Authentication functionality for Administrator/User
* Managing cities, adresses and users directly from website
* Changed admin page for comfortable managing


## Demo
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/590f49fc-3ce4-4103-86eb-b88ef184f187)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/86c48201-04d2-4617-b997-c3ebf903df24)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/fc028341-f7f3-4c34-8bc0-87a5cd0506fa)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/686ece8d-0b02-45c7-b3ae-27ddc81a81ae)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/bc043ffe-53c3-4955-9e70-7b0d11f94bcb)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/d8f04ac2-6fbd-4cca-940a-29bc77657ebf)

## Installation

Python3 must be already installed


```shell
git clone https://github.com/niksgawrilenko/internet-services-management-platform
cd internet-services-management-platform
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate #create data base
python manage.py runserver # starts Django server
```
