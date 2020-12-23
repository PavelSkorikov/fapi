# fapi

Web app, where get employees list by company

## Requirements
Docker, Docker-compose

## Usage
To run the server, please clone this git repository and open project directory
```
git clone https://github.com/PavelSkorikov/fapi.git
cd fapi
```
execute the following commands:
```
docker-compose -f docker-compose.dev.yml up --build
```

## API:
```.env
    /api/employees/?company=Company_name
        receive data:
            - list employees by company
```
    
