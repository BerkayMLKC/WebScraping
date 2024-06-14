<!DOCTYPE html>
<html>
<head>
<title>Database ile urun listesi</title>
<style>
table {
border-collapse: collapse;
width: 100%;
color: #AFAFFC;
font-family: cursive;
font-size: 25px;
text-align: left;
}
th {
background-color: #AFAFFC;
color: white;
}
tr:nth-child(even) {background-color: #EFEFFF}
</style>
</head>
<body>
<table>
<tr>
<th>PC Grupları</th>
<th>Özellikler</th>
<th>Özellikler</th>
<th>Fiyat</th>
<th>Adres  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Urunler 6 lı ve 10 lu id grupları halinde sıralanmıştır</th>
</tr>
<?php
$baglanti = mysqli_connect("localhost", "root", "19875300cC.f", "prolan");

if ($baglanti->connect_error) {
die("Baglanti hatasi: " . $baglanti->connect_error);
}

function urlALma($girdi){
    $bul = array('`((?:https?|ftp)://\S+[[:alnum:]]/?)`si', '`((?<!//)(www\.\S+[[:alnum:]]/?))`si');
    $degis = array('<a href="$1" target="_blank">$1</a>', '<a href="http://$1" target="_blank">$1</a>');
    return preg_replace($bul,$degis,$girdi);
}


$k=0;
for ($i=0 ; $i<750 ; $i++) {
    $i=$k;

    for ($j=0 ; $j<6 ; $j++) {
        $sql = $baglanti->query("SELECT * FROM tablo WHERE num= $i+1");
        $sonuc = $sql->fetch_assoc();
        $kelime = urlAlma($sonuc["linkk"]);
        echo "<tr><td>" . $sonuc["num"]. "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" . "</td><td>" . $sonuc["bilgisayar"]. "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" 
        . "</td><td>" . $sonuc["ozel1"]. "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" . "</td><td>"
        . $sonuc["fiyat"]. "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" . "</td><td>" . $kelime. "</td><td>";
        $i=$i+1;
        $k=$i;
    }     
    #echo "<tr><td>" . "</td><td>" . "</td><td>" . "</td><td>" . "Diğer Bilgisayar" ."</td><tr>";     
}


$baglanti->close();
?>
</table>
</body>
</html>