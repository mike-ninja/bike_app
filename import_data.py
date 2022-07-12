# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    import_data.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbarutel <mbarutel@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/11 13:21:41 by mbarutel          #+#    #+#              #
#    Updated: 2022/07/11 13:42:01 by mbarutel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyodbc
import pandas as pd

data = pd.read_csv("/Users/mike_barutel/Desktop/solita/csv/test.csv")
df = pd.DataFrame(data, columns= ["Departure station name", "Return station name"])
conn = pyodbc.connect(
'Driver={SQL Server};'
'Server={SQL Server};'
'Database=bikeapp;'
'Trusted_Connection=yes;'
)
print (df)
