# UI, API and Mobile Automation Framework

A Python test automation project covering web UI, REST APIs and an Android app.

## Tech Stack
- Python and Pytest
- Playwright — web UI testing
- Requests — API testing
- Appium with UiAutomator2 — Android testing
- Allure — test reporting
- GitHub Actions — automated CI runs

## Test Coverage
- 9 UI tests: SauceDemo login and inventory
- 2 API tests: ReqRes user endpoints
- 2 mobile tests: valid and invalid login in Sauce Labs My Demo App

## Setup on Windows

Install Python, Git and the Allure command-line tool.

Clone the repository and enter the project folder:

```powershell
git clone https://github.com/shruthi-kallimath/ui-api-automation-framework.git
cd ui-api-automation-framework\qa-ui-api-framework
```

Create a virtual environment and install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe -m playwright install chromium
```

All commands below run from the `qa-ui-api-framework` folder.

## Run UI Tests

```powershell
.\venv\Scripts\python.exe -m pytest tests/ui -v -p no:cacheprovider --alluredir=allure-results-ui
```

## Run API Tests

```powershell
.\venv\Scripts\python.exe -m pytest tests/api -v -p no:cacheprovider --alluredir=allure-results-api
```

The API tests require network access to ReqRes. Any API key required by the service must be supplied through the test configuration.

## Android Setup

Install Android Studio, an Android emulator, Node.js and Java 17.
Configure `ANDROID_HOME` and `JAVA_HOME`.

Install Appium and its Android driver:

```powershell
npm.cmd install -g appium@3.8.0
appium.cmd driver install uiautomator2@8.7.0
```

Start an emulator and confirm its device ID:

```powershell
& "$env:ANDROID_HOME\platform-tools\adb.exe" devices
```

The mobile fixture expects `emulator-5554`.

Download the demo APK:
https://github.com/saucelabs/my-demo-app-rn/releases/download/v1.3.0/Android-MyDemoAppRN.1.3.0.build-244.apk

Install it, replacing the example path with your downloaded APK path:

```powershell
& "$env:ANDROID_HOME\platform-tools\adb.exe" -s emulator-5554 install -r "C:\path\to\Android-MyDemoAppRN.1.3.0.build-244.apk"
```

Start Appium in a separate terminal and leave it running:

```powershell
appium.cmd --address 127.0.0.1 --port 4723
```

## Run Mobile Tests

With the emulator and Appium running:

```powershell
.\venv\Scripts\python.exe -m pytest tests/mobile -v -p no:cacheprovider --alluredir=allure-results-mobile
```

## Run All Tests

With the emulator and Appium running:

```powershell
.\venv\Scripts\python.exe -m pytest tests/ui tests/api tests/mobile -v -p no:cacheprovider --alluredir=allure-results-final
```

## View Allure Reports

Use the results folder from the corresponding test run:

```powershell
allure serve allure-results-ui
allure serve allure-results-api
allure serve allure-results-mobile
allure serve allure-results-final
```

## GitHub Actions

- UI and API tests run on pushes and pull requests, and can be started manually.
- Android tests can be started manually through Actions → Android Appium Tests → Run workflow.
- Test results are uploaded as downloadable workflow artifacts.

## Scope

The mobile tests demonstrate login success and rejection of invalid credentials. 
