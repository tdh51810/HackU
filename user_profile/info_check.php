<?php
$username = $_POST['username'];          #利用者本人の名前
$sex = $_POST['sex'];
$address = $_POST['address'];            #都道府県1:北海道2:青森...http://elze.tanosii.net/d/kenmei.htm
$father = $_POST['father'];
$mother = $_POST['mother'];
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
$slacktoken = $_POST['slacktoken'];      #slackのトークンID
$slackchannel = $_POST['slackchannel'];  #投稿先チャンネルのslackID
$slack_toname = $_POST['slack_toname'];  #休みを申告する所属先の名前
$time = $_POST['time'];                  #通勤時間

$user = array("名前" => $username,"性別" => $sex,"住所" => $address, "父親" => $father, "母親" => $mother, "祖父" => $g_father,"祖母" => $g_mother,"兄" => $brother1,"姉" => $sister1, "弟" => $brother2,"妹" => $sister2,"叔父" => $uncle, "叔母" => $aunt, "いとこ" => $cousin, "ペット" => $pet, "トークン" => $slacktoken, "チャンネル" => $slackchannel,"申告先" => $slack_toname,"通勤時間" => $time);

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
    <script>
      function info_check(){
        window.location.href = "./info_write.php";
      }
    </script>
  </head>
  <body>
　　　　<h1>確認画面</h1>
    <p>以下のような文面で、指定したチャンネルに投稿されます。<FONT color="red">よろしければ登録ボタンを、内容を変更したい場合は前のページに戻ってください。</FONT></p>

    <div id=post_text>
        <?=$slack_toname?>の皆様<br><br>
        おはようございます。<?=$slack_toname?>所属の<?=$username?>です。<br><br>風邪を引いてしまったため、休ませていただきます。<br>申し訳ありませんが、よろしくお願いいたします。<br>
    </div><br><br>


   <form name="check">   
     <input type="button" value="登録" onClick="info_check()">
   </form> 


<footer>
Copyright &copy 山形大学工学部情報科学科井上研究室 All Rights Reserved.
</footer>
  </body>
</html>

