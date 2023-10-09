# Internet Services Management Platform

#### Django project for providing ISP services.

![InternetServicesManagementPlatform  drawio](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/e55d786d-98d8-472d-8559-46f8d8173b58)

### Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata load.json`

### After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin`
  - Password: `1qazcde3`
### Credentials of the test user
  - Login: `test_user`
  - Password: `1qazcde3`
## Features
### Main functionality:
* Authentication functionality for Administrator/User
* Managing cities, addresses and users directly from website
* Changed admin page for comfortable managing
### Additional functionality:
* Ability to search lists of users, cities, addresses, tariffs.
* Ability for the user to connect toan address with one click of a button.
* Ability for the user to connect a tariff at the touch of a button.

## Demo
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/590f49fc-3ce4-4103-86eb-b88ef184f187)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/2ace8e33-decd-486e-a645-58b70c9fdfe9)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/fc028341-f7f3-4c34-8bc0-87a5cd0506fa)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/92afc4db-a771-423a-9d22-7c2f8e4535db)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/9248dcaa-1d57-487b-8b5f-d62c1084b3b5)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/bc043ffe-53c3-4955-9e70-7b0d11f94bcb)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/d8f04ac2-6fbd-4cca-940a-29bc77657ebf)

## Installation

Python3 must be already installed


```shell
git clone -b develop https://github.com/niksgawrilenko/internet-services-management-platform
cd internet-services-management-platform
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate #create data base
python manage.py runserver # starts Django server
```
