# sharecode
Super simple prototype of sharecode

## Getting Started

### Prerequisites

* Python 3.9

### Installing
1. Clone this repository
```bash
git clone https://github.com/gwanryo/sharecode.git
```

2. (Optional) Create venv in repository folder
```bash
py -m venv .venv
```

3. Install requirements
```bash
py -m pip install -r requirements.txt
```

4. Init database, then migrate and upgrade
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Check there is 'sharecode.db' in repository folder

6. Run server
```bash
flask run
```
