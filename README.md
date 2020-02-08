# Investment

Crawling financial data and plan to analyze the data for future investment

Focus on ASX

## Getting Started

Recommed creating a virtual environment for this project


#### Create virtual environment

MacOS
```
python -m venv venv
```
Windows
```
py -m venv venv
```

#### Activate `venv`
MacOS
```
source venv/bin/activate
```
Windows
```
.\venv\Scripts\activate
```

#### Install all required packages from requirements.txt
```
pip install -r requirements.txt
```

#### *If you want to deactivate the virtual environment
```
deactivate
```

#### Require the chrome driver that matches your browser version 
https://chromedriver.chromium.org/downloads

Extract and put into

MacOS: `venv/bin/`

Windows: `venv\Scripts\`


## Run

Base on trading volumn, get the top 500 trading volumn stocks and its url in ASX
```
python main.py
```

## To Do

use the url to get companies' financial summary
