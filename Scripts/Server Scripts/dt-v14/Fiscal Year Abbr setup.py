s = doc.exp_start_date    # Data taken from the required date
t_year = s[2:4]
t_month = s[5:7]
t_day = s[8:]

if int(t_month) < 4:
    if t_year == '00':
        doc.fiscal_year_abbr = 99
    else:
        doc.fiscal_year_abbr = int(t_year) - 1
else :
    doc.fiscal_year_abbr = t_year
