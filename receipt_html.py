receipt_table_dev = """
<html>
        <head><title>Predračun</title></head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <link rel="stylesheet" type="text/css" href="table_style.css"/>
        <body>
            <div>
                <div class="inline-block">
                    <img src="logo.png">
                    <img src="kontakt.png">
                </div>
            </div>
            <center class="dataframe fontstyle"><strong>PREDRAČUN</strong></center>
            <p align="right" class="dataframe datefontstyle"><right><strong>DANA:{todays_date}</strong></right></p>
            <table border="1" class="dataframe customerstyle">
    <thead>
        <tr style="text-alight: left;">
        <th>IME I PREZIME</th>
        <th class="dataframe normalfont">{customer_name}</th>
    </thead>
    <tbody>
        <tr>
        <td>MARKA I MODEL VOZILA</td>
        <td class="dataframe normalfont">{customer_car}</td>
        </tr>
        <tr>
        <td>REGISTARSKI BROJ</td>
        <td class="dataframe normalfont">{customer_reg}</td>
        </tr>
    </tbody>
            {to_browser}
            <table border="1" class="dataframe mystyle">
    <thead>
        <tr style="text-align: center;">
        <th>RAD[KM]</th>
        <th>DIJELOVI TOTAL[KM]</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td class="dataframe normalfont">{work_price}</td>
        <td class="dataframe normalfont">{total_price}</td>
        </tr>
    </tbody>
            <table border="1" class="dataframe mystyle">
    <thead>
        <tr style="text-align: center;">
        <th>TOTAL CIJENA[KM]</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td class="dataframe normalfont">{final_price}</td>
        </tr>
    </tbody>
        </body>
    </html>
"""
receipt_table_release = """
<html>
        <head><title>Predračun</title></head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <link rel="stylesheet" type="text/css" href="_internal/table_style.css"/>
        <body>
            <div>
                <div class="inline-block">
                    <img src="_internal/logo.png">
                    <img src="_internal/kontakt.png">
                </div>
            </div>
            <center class="dataframe fontstyle"><strong>PREDRAČUN</strong></center>
            <p align="right" class="dataframe datefontstyle"><right><strong>DANA:{todays_date}</strong></right></p>
            <table border="1" class="dataframe customerstyle">
    <thead>
        <tr style="text-alight: left;">
        <th>IME I PREZIME</th>
        <th class="dataframe normalfont">{customer_name}</th>
    </thead>
    <tbody>
        <tr>
        <td>MARKA I MODEL VOZILA</td>
        <td class="dataframe normalfont">{customer_car}</td>
        </tr>
        <tr>
        <td>REGISTARSKI BROJ</td>
        <td class="dataframe normalfont">{customer_reg}</td>
        </tr>
    </tbody>
            {to_browser}
            <table border="1" class="dataframe mystyle">
    <thead>
        <tr style="text-align: center;">
        <th>RAD[KM]</th>
        <th>DIJELOVI TOTAL[KM]</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td class="dataframe normalfont">{work_price}</td>
        <td class="dataframe normalfont">{total_price}</td>
        </tr>
    </tbody>
            <table border="1" class="dataframe mystyle">
    <thead>
        <tr style="text-align: center;">
        <th>TOTAL CIJENA[KM]</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td class="dataframe normalfont">{final_price}</td>
        </tr>
    </tbody>
        </body>
    </html>
"""

receipt_data_header = """<table border="1" class="dataframe mystyle">
  <thead>
    <tr style="text-align: center;">
      <th>Materijal</th>
      <th>Marka</th>
      <th>Cijena[KM]</th>
      <th>Količina</th>
      <th>Ukupno[KM]</th>
    </tr>
  </thead>
  {materials}
</table>"""

receipt_data = '''<tbody>
    <tr>
      <td class="dataframe normalfont">{material}</td>
      <td class="dataframe normalfont">{model}</td>
      <td class="dataframe normalfont">{price}</td>
      <td class="dataframe normalfont">{amount}</td>
      <td class="dataframe normalfont">{final_price}</td>
    </tr>
  </tbody>'''