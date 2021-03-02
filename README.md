# py-one-time-pad

Simple one-time pad encryption made with python 3. This program uses **bitarray** library.

## Requirements

- Python3
- Python package manager (pip)

## Installation

Use the package manager **pip** to install the requirements:

```
pip install -r requirements.txt
```

## Usage

1. Clone this repo
2. With your terminal, go to the repo directory

### Cypher a message

- Run the following command

```
python main.py -c
```

or else

```
python main.py --cypher
```

This will generate two files:

- cyphered.txt: this will contain your message cyphered in bits.
- key.txt: the key used to cypher (and decypher) your message.

### Decypher a message

- First, you'll need two files:
  - One containing your message (input file)
  - Another one containing your key (key file)
- Run the following command:

```
python main.py -d -i <input file> -k <key file>
```

or else

```
python main.py --decypher --inputfile=<input file> --keyfile=<key file>
```

## Developer:

- Oscar Juárez

Universidad del Valle de Guatemala - 2021
