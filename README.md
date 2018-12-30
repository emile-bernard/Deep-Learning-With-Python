
# Deep-Learning-With-Python

## Description

My version of the examples in the Deep Learning With Python book by François Chollet.

## Setup

1. Install Python
```
python3 --version
pip3 --version
virtualenv --version
```

```
sudo apt update
sudo apt install python3-dev python3-pip
sudo pip3 install -U virtualenv  # system-wide-install
```

2. Create a virtual environment
```
virtualenv --system-site-packages -p python3 ./venv

source ./venv/bin/activate  # sh, bash, ksh, or zsh
```

```
(venv) pip install --upgrade pip
(venv) pip list  # show packages installed within the virtual environment
(venv) deactivate  # don't exit until you're done using TensorFlow
```

3. Install the TensorFlow pip package
```
(venv) pip install --upgrade tensorflow

(venv) python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))" # verify the install
```

## Run

Run each .py file as a python script.

```
source ./venv/bin/activate

python example.py
```

## Technology Used

- [Python 3.7.2](https://www.python.org/)

- [Keras 2.0.8](https://faroit.github.io/keras-docs/2.0.8/)

- [p2.xlarge EC2 instance](https://aws.amazon.com/fr/ec2/instance-types/p2/)

- [Tensorflow package](https://www.tensorflow.org/install/pip)

## Links

- [Deep Learning With Python Notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks)

- [Deep Learning With Python Amazon](https://www.amazon.ca/dp/1617294438/ref=cm_sw_r_cp_apa_i_SfdjCb4CFBTJX)
