# Host Connections Tool

With this program, given a logs report as .txt file, you can filter the connections made to a specific host in a specific period of time.

## Installation

We only need Python to run the code, no external libraries are needed.

## Usage

Run the python code called 'hostool.py' by running the following command on a Terminal:
```python
python hostool.py
```
Script can be executed double clicking hostool.bat on Windows.

Four user inputs are asked on console:

- **txt_filename**: The name of the dataset we are going to analyze, without the extension.
- **init_datetime**: The date and time you want to start from searching host connections. *Format example '01/01/2000 00:00:00' needed.*
- **end_datetime**: The limit date and time you want to reach searching host connections. *Format example '01/01/2000 00:00:00' needed.*
- **hostname**: The name of the host you want to find connections made with.

After entering inputs, the program will find the connected hosts to **hostname** one in a range between **init_datetime** and **end_datetime** using the **txt_filename** name to search the required dataset. This in an example of a default output:

```python
------------ Agapito LOG ------------
Connections made in the time range you have selected:

2019-08-13 00:51:24 Zihanna - Agapito
2019-08-13 02:50:03 Kenidy - Agapito
2019-08-13 05:21:17 Asmar - Agapito
2019-08-13 07:47:43 Dragon - Agapito
2019-08-13 09:13:45 Monet - Agapito
2019-08-13 11:31:17 Keierra - Agapito
2019-08-13 13:23:47 Jordee - Agapito
2019-08-13 15:51:52 Kaydenn - Agapito
2019-08-13 16:40:40 Jahmire - Agapito
2019-08-13 20:33:25 Danaria - Agapito
2019-08-13 20:56:28 Joselina - Agapito
2019-08-13 22:38:58 Katriece - Agapito
2019-08-13 22:59:03 Liviana - Agapito
```

## About

Development made as a test for a Data and Technical Operations Engineer open position for Clarity AI.