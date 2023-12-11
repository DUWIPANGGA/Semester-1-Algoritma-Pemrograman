bulan=['januari','februari','maret','april','juni','juli','agustus','september','oktober','november','desember']

INPUT=input('enter a date (mm/dd/yyyy): ')
date=INPUT.split('/')

print('the converted date is:',bulan[int(date[0])],date[1],',',date[2])