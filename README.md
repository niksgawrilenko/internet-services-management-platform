# Internet Services Management Platform

The Internet Services Management Platform is a web application based on Django, designed to manage subscriptions to internet services, customers, tariffs, addresses, and cities. It provides a convenient way to organize and manage services for an internet service provider.

## Check it out!
[Internet Services Management Platform deployed to Render](https://internet-services-management-platform-isp.onrender.com)

### Credentials of the test user
  - Login: `test_user`
  - Password: `1qazcde3`

## ![InternetServicesManagementPlatform  drawio](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/e55d786d-98d8-472d-8559-46f8d8173b58)

## Functionality

- **Customer Management:**
  - Create, view, update, and delete customer profiles.
  - Assign tariffs to customers.
  - Track customer balances.

- **Tariff Management:**
  - Define various internet service tariffs with different speeds and prices.
  - Connect and disconnect tariffs for customers.

- **Address Management:**
  - Add, edit, and delete customer addresses.
  - Associate addresses with customers.

- **City Management:**
  - Maintain a list of cities where internet services are provided.
  - Add, edit, and delete cities.

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
### Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata load.json`

### Setting environment variables:

For Unix systems (Linux, macOS):
```shell
echo "SECRET_KEY=my_secret_key" > .env
echo "DEBUG=True" >> .env
```
For Windows:
```shell
echo SECRET_KEY=my_secret_key > .env
echo DEBUG=True >> .env
```
## Demo
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/590f49fc-3ce4-4103-86eb-b88ef184f187)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/2ace8e33-decd-486e-a645-58b70c9fdfe9)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/fc028341-f7f3-4c34-8bc0-87a5cd0506fa)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/92afc4db-a771-423a-9d22-7c2f8e4535db)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/9248dcaa-1d57-487b-8b5f-d62c1084b3b5)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/bc043ffe-53c3-4955-9e70-7b0d11f94bcb)
![image](https://github.com/niksgawrilenko/internet-services-management-platform/assets/90038040/d8f04ac2-6fbd-4cca-940a-29bc77657ebf)

## Reporting Issues
If you encounter any problems or have suggestions for improvements, please open an issue on the GitHub repository.

## License
By contributing your code, you agree to license your contribution under the terms of the [License](LICENSE.md).
