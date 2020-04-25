# Script Queue Manager
A simple library to display an eta bar. Useful to track the progress of long running tasks. It can be included in the project with just 2 lines of code.

## Installing from pip

### Stable release
```shell script
pip install etabar
```

### Development release
```shell script
pip install -i https://test.pypi.org/simple/ etabar
```

### Example usage
```python
from etabar.ETA import ETA
import time

eta = ETA(100)
time.sleep(2)
for i in range(100):
    eta.update()
    time.sleep(2)
```

## Getting Started
I highly recommend that you fork the project by clicking on the ``Fork`` button and then cloning your fork using the command mentioned below.

``
git clone <your fork URL>
`` 

### Prerequisites
- Python 3.5+
- A code editor or IDE(preferable PyCharm)

### Setting up for Development
Follow the steps mentioned below to get your dev instance running.

1) After cloning your fork, open the project in an IDE or code editor of you choice.

1) It is highly advisable that you create a new Python environment for the project. Follow the instructions given [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands).

1) Navigate to the project directory and install the `requirement.txt` packages.
    ```shell script
    cd <project-directory>
    pip install -r requirements.txt
    ```
   
## Tests
Not yet implemented

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Mayank Vaidya** - *Initial work*

See also the list of [contributors](contributors.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
