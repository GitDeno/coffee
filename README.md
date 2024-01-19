# Coffee blog template

This is a simple blog template that I created for the purpose of practicing my skills in the Django framework. 

## Installation

To run "Coffee blog" locally, follow these steps:

- Clone the repository:

```
git clone https://github.com/GitDeno/coffee.git
```

- Create a Python virtual environment and activate it:
```
python -m venv venv
```
- Run virtual environment
```
venv/Scripts/activate
```
- Install the required dependencies:
```
pip install -r requirements.txt
```
- Find the file "env.example" and, following it in the same location, create a file named ".env"

- Change directory using terminal to "coffee/" and perform database migrations:
```
python manage.py migrate
```
- Run Django server using:
```
python manage.py runserver
```
## Usage



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
