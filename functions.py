# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:35:25 2024

@author: jferenc
"""

import pandas as pd
import numpy as np
import re
import os
import logging
from datetime import date, datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.fernet import Fernet



def send_email(sender: str, receivers: str, subject: str, body: str, host: str='localhost', port: int=0):
    '''
    Sends an email from a given sender to given receivers. 

    Parameters
    ----------
    sender : str
        Email address of the sender.
    receivers : str
        Email addresses of the receivers. Separated by comma if more than one.
    subject : str
        Subject of the email.
    body : str
        Content of the email.
    host : str
        Hostname used to create an SMTP connection.
    port : int
        Port used to create an SMTP connection.

    Returns
    -------
    None.

    '''

    # creating an instance of MIMEMultipart() to build an email message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receivers
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # establishing a connection to the SMTP server
    server = smtplib.SMTP(host, port)
    server.ehlo()
    # securing the connection
    server.starttls()
    server.ehlo()
	
    # sending the message
    server.send_message(msg)
    server.quit()
	
    return None


def get_logger(log_dir: str='.\\logs\\', log_filename: str=''):
    '''
    Sets up a logger that will save logs in a specified location.

    Parameters
    ----------
    log_dir : str
        The directory where the log files should be saved.
    log_filename : str
        The beginning of the name of the log file (typically, it is the name of the script that is run).
        Later in the script timestamp is generated and added at the end of the log's filename.

    Returns
    -------
    logger

    '''
    
    # create a log directory if it doesn't exist yet
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

	# create a log filename ending with with the current timestamp
    timestamp = str(int(datetime.timestamp(datetime.now())))
    if log_filename == '':
        log_output_file = log_dir + 'log_' + timestamp + '.log' 
    else:
        log_output_file = log_dir + log_filename + '_log_' + timestamp + '.log'
	
    # set up logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
    fh = logging.FileHandler(log_output_file, mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
	
    return logger


def Fernet_decrypt(encrypted_password: str, key: str=b'jW8zeJU1b62evmyHNqyAGxUYMs2_5pK4jDSB_BCzBI4='):
    '''
    Decrypts an encrypted password using the Fernet encryption algorithm.
    This method is used to avoid the hardcoding of some of the passwords.

    Parameters
    ----------
    encrypted_password : str
        Encrypted password that needs to be decrypted.
    encrypted_password : str, optional
        The key used for encryption/decryption.

    Returns
    -------
    decrypted_password

    '''

    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
	
    return decrypted_password
	

def day_ago(number: int=1, format: str='%Y%m%d'):
    '''
    Returns the string for date a given number of days ago

    Parameters
    ----------
    number : int, optional
        Number of days ago. The default is 1.
    format : str, optional
        Format of the output date. The default is '%Y%m%d'.

    Returns
    -------
    date

    '''   
    
	# get a date n days before
    today = date.today()
    today = datetime.combine(today, datetime.min.time())
    day = today - timedelta(days=number)
    
    return day.strftime(format)


def month_ago(number: int=1, format: str="%Y-%m"):
    '''
    Returns the string for month a given number of months ago

    Parameters
    ----------
    number : int, optional
        Number of months ago. The default is 1.
    format : str, optional
        Format of the output month. The default is '%Y-%m'.

    Returns
    -------
    month

    '''   
	
	# get previous month (for which we want data)
    today = date.today()
    today = datetime.combine(today, datetime.min.time())
    month = today - timedelta(months=number)
	
    return month.strftime(format)