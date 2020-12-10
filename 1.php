Hello!

<form method=get>
Как вас зовут?
<input name=name >
Сколько вам лет?
<input name=age >
<button type=submit>
GO!
</button>
</form>

<?php
$name=$_POST('name');
$age=$_POST('age');
echo "Привет, $name, через 10 лет вам будет ".$age+10 ;
?>

Good bye
