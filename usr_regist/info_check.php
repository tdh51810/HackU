<?php
$username = $_POST['username'];          #利用者本人の名前
$sex = $_POST['sex'];
$address = $_POST['address'];            #都道府県1:北海道2:青森...http://elze.tanosii.net/d/kenmei.htm
$spouse = $_POST['spouse'];              #配偶者(一夫多妻制などに対応済み)
$children = $_POST['children'];          #子供の人数
$father = $_POST['father'];              #父親の人数(ジェンダー的な問題に対応)
$mother = $_POST['mother'];              #母親の人数(同上)
$g_father = $_POST['g_father'];
$g_mother = $_POST['g_mother'];
$brother1 = $_POST['brother1'];          #兄
$sister1 = $_POST['sister1'];            #姉
$brother2 = $_POST['brother2'];          #弟 
$sister2 = $_POST['sister2'];            #妹
$uncle = $_POST['uncle'];                #叔父
$aunt = $_POST['aunt'];                  #叔母
$cousin = $_POST['cousin'];              #いとこ
$pet = $_POST['pet'];                    #ペット
$holiday = $_POST['holiday'];            #残り有給休暇数
$userid = $_POST['userid'];              #slackのユーザID
$slacktoken = $_POST['slacktoken'];      #slackのトークンID
$slackchannel = $_POST['slackchannel'];  #投稿先チャンネルのslackID

$user = array("名前" => $username,"性別" => $sex,"住所" => $address,"配偶者" => $spouse,"子ども" =>$children, "父親" => $father, "母親" => $mother, "祖父" => $g_father,"祖母" => $g_mother,"兄" => $brother1,"姉" => $sister1, "弟" => $brother2,"妹" => $sister2,"叔父" => $uncle, "叔母" => $aunt, "いとこ" => $cousin, "ペット" => $pet,"有給休暇" => $holiday,"ユーザid" => $userid, "トークン" => $slacktoken, "チャンネル" => $slackchannel);

$filename = "./user_check.txt";
$output ="";

foreach($user as $key => $value){
$output .= '"'.$key.'"' . ":" . '"'.$value.'"'.",";
}
$output = substr($output,0,-1);
$output = "{".$output."}";
file_put_contents($filename, $output);
?>
<!DOCTYPE html>
<html>
  <head>
    <title>確認画面</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="check.css">
    <script>
      function info_check(){
        window.location.href = "./info_write.php";
      }
    </script>
  </head>
  <body>
   
    <header>
      <div id ="logo"><img src="./image/logo.png" width ="80px" height="80px" style="float:left;"></div>
　　　　  <h1 id="title">確認画面</h1>
    </header>

    <div id="main" style="clear:both;">
    <p>以下のような文面で、指定したチャンネルに投稿されます。<FONT color="red">よろしければ登録ボタンを、内容を変更したい場合は前のページに戻ってください。</FONT></p>
 
    <h2>文面例</h2>
    <div id="post_text">
        おはようございます。<?=$username?>です。<br><br>風邪を引いてしまったため、休ませていただきます。<br>申し訳ありませんが、よろしくお願いいたします。<br>
    </div><br><br>


   <form name="check">   
     <input type="button" value="登録" onClick="info_check()">
   </form> 
   </div>

<div id="footer">
Copyright &copy 山形大学工学部情報科学科井上研究室 All Rights Reserved.
</div>
  </body>
</html>

