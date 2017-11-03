from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = ""
password = ""
from_email = username

with open('emails.txt') as f:
    to_list = [email.strip() for email in f]

msg_root = MIMEMultipart('related')
msg_root['Subject'] = 'Travel Lab | Лаборатория Путешествий. Предложение по сотрудничеству'
msg_root['From'] = from_email
msg_root['To'] = ''
msg_root.preamble = 'multipart message in MIME format'

msg_alternative = MIMEMultipart('alternative')
msg_root.attach(msg_alternative)

msg_text = MIMEText('alternative plain text message')
msg_alternative.attach(msg_text)


html_txt = """\
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="format-detection" content="telephone=no" />
    <title>Travel Lab | Лаборатория Путешествий</title>
    <style type="text/css">
      html { background-color:#E1E1E1; margin:0; padding:0; }
      body, #bodyTable, #bodyCell, #bodyCell{height:100% !important; margin:0; padding:0; width:100% !important;font-family:Helvetica, Arial, "Lucida Grande", sans-serif;}
      table{border-collapse:collapse;}
      table[id=bodyTable] {width:100%!important;margin:auto;max-width:500px!important;color:#7A7A7A;font-weight:normal;}
      img, a img{border:0; outline:none; text-decoration:none;height:auto; line-height:100%;}
      a {text-decoration:none !important;border-bottom: 1px solid;}
      h1, h2, h3, h4, h5, h6{color:#5F5F5F; font-weight:normal; font-family:Helvetica; font-size:20px; line-height:125%; text-align:Left; letter-spacing:normal;margin-top:0;margin-right:0;margin-bottom:10px;margin-left:0;padding-top:0;padding-bottom:0;padding-left:0;padding-right:0;}
      .ReadMsgBody{width:100%;} .ExternalClass{width:100%;}
      .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{line-height:100%;}
      table, td{mso-table-lspace:0pt; mso-table-rspace:0pt;}
      #outlook a{padding:0;}
      img{-ms-interpolation-mode: bicubic;display:block;outline:none; text-decoration:none;}
      body, table, td, p, a, li, blockquote{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%; font-weight:normal!important;}
      .ExternalClass td[class="ecxflexibleContainerBox"] h3 {padding-top: 10px !important;}
      h1{display:block;font-size:26px;font-style:normal;font-weight:normal;line-height:100%;}
      h2{display:block;font-size:20px;font-style:normal;font-weight:normal;line-height:120%;}
      h3{display:block;font-size:17px;font-style:normal;font-weight:normal;line-height:110%;}
      h4{display:block;font-size:18px;font-style:italic;font-weight:normal;line-height:100%;}
      .flexibleImage{height:auto;}
      .linkRemoveBorder{border-bottom:0 !important;}
      table[class=flexibleContainerCellDivider] {padding-bottom:0 !important;padding-top:0 !important;}
      body, #bodyTable{background-color:#E1E1E1;}
      #emailHeader{background-color:#E1E1E1;}
      #emailBody{background-color:#FFFFFF;}
      #emailFooter{background-color:#E1E1E1;}
      .nestedContainer{background-color:#F8F8F8; border:1px solid #CCCCCC;}
      .emailButton{background-color:#205478; border-collapse:separate;}
      .buttonContent{color:#FFFFFF; font-family:Helvetica; font-size:18px; font-weight:bold; line-height:100%; padding:15px; text-align:center;}
      .buttonContent a{color:#FFFFFF; display:block; text-decoration:none!important; border:0!important;}
      .emailCalendar{background-color:#FFFFFF; border:1px solid #CCCCCC;}
      .emailCalendarMonth{background-color:#205478; color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; padding-top:10px; padding-bottom:10px; text-align:center;}
      .emailCalendarDay{color:#205478; font-family:Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold; line-height:100%; padding-top:20px; padding-bottom:20px; text-align:center;}
      .imageContentText {margin-top: 10px;line-height:0;}
      .imageContentText a {line-height:0;}
      #invisibleIntroduction {display:none !important;}
      span[class=ios-color-hack] a {color:#275100!important;text-decoration:none!important;}
      span[class=ios-color-hack2] a {color:#205478!important;text-decoration:none!important;}
      span[class=ios-color-hack3] a {color:#8B8B8B!important;text-decoration:none!important;}
      .a[href^="tel"], a[href^="sms"] {text-decoration:none!important;color:#606060!important;pointer-events:none!important;cursor:default!important;}
      .mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {text-decoration:none!important;color:#606060!important;pointer-events:auto!important;cursor:default!important;}
      @media only screen and (max-width: 480px){
          body{width:100% !important; min-width:100% !important;}
          table[id="emailHeader"],
          table[id="emailBody"],
          table[id="emailFooter"],
          table[class="flexibleContainer"],
          td[class="flexibleContainerCell"] {width:100% !important;}
          td[class="flexibleContainerBox"], td[class="flexibleContainerBox"] table {display: block;width: 100%;text-align: left;}
          td[class="imageContent"] img {height:auto !important; width:100% !important; max-width:100% !important; }
          img[class="flexibleImage"]{height:auto !important; width:100% !important;max-width:100% !important;}
          img[class="flexibleImageSmall"]{height:auto !important; width:auto !important;}
          table[class="flexibleContainerBoxNext"]{padding-top: 10px !important;}
          table[class="emailButton"]{width:100% !important;}
          td[class="buttonContent"]{padding:0 !important;}
          td[class="buttonContent"] a{padding:15px !important;}
      }
      @media only screen and (-webkit-device-pixel-ratio:.75){
          /* Put CSS for low density (ldpi) Android layouts in here */
      }
      @media only screen and (-webkit-device-pixel-ratio:1){
          /* Put CSS for medium density (mdpi) Android layouts in here */
      }
      @media only screen and (-webkit-device-pixel-ratio:1.5){
          /* Put CSS for high density (hdpi) Android layouts in here */
      }
      @media only screen and (min-device-width : 320px) and (max-device-width:568px) {
      }
    </style>
    <!--[if mso 12]>
      <style type="text/css">
          .flexibleContainer{display:block !important; width:100% !important;}
      </style>
    <![endif]-->
    <!--[if mso 14]>
      <style type="text/css">
          .flexibleContainer{display:block !important; width:100% !important;}
      </style>
    <![endif]-->
  </head>
  <body bgcolor="#E1E1E1" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">
    <center style="background-color:#E1E1E1;">
      <table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="table-layout: fixed;max-width:100% !important;width: 100% !important;min-width: 100% !important;">
        <tr>
          <td align="center" valign="top" id="bodyCell">
            <table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailHeader">
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <table border="0" cellpadding="10" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td valign="top" width="500" class="flexibleContainerCell">
                            <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
                              <tr>
                                <td align="left" valign="middle" id="invisibleIntroduction" class="flexibleContainerBox" style="display:none !important; mso-hide:all;">
                                  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
                                    <tr>
                                      <td align="left" class="textContent">
                                        <div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
                                            Предложение о сотрудничестве
                                        </div>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                                <td align="right" valign="middle" class="flexibleContainerBox">
                                  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
                                    <tr>
                                      <td align="left" class="textContent">
                                        <!-- CONTENT // -->
                                        <div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
                                            Если вы не видете это сообщение, <a href="#" target="_blank" style="text-decoration:none;border-bottom:1px solid #828282;color:#828282;"><span style="color:#828282;">откройте его в браузере</span></a>.
                                        </div>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
            <table bgcolor="#FFFFFF"  border="0" cellpadding="0" cellspacing="0" width="500" id="emailBody">
              <!-- header -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td valign="top" width="500" class="flexibleContainerCell">
                              <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                  <td align="left" valign="top" class="flexibleContainerBox">
                                    <table border="0" cellpadding="0" cellspacing="0" width="210" style="max-width: 100%;">
                                      <tr>
                                        <td valign="top" class="imageContent">
                                          <a href="http://www.travellab.by/?utm_source=email_distribution"><img src="cid:logo" width="500" class="flexibleImage" style="max-width:500px;width:100%;display:block;" alt="Travel Lab" title="Travel Lab" /></a>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                  <td align="right" valign="middle" class="flexibleContainerBox">
                                    <table class="flexibleContainerBoxNext" border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                      <tr>
                                        <td align="left" class="textContent">
                                          <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                            +375-29-369-45-89<br/>
                                            +375-29-777-97-23<br/>
                                            +375-25-901-67-06<br/>
                                            <a class="mobile_link" href="mailto:travellabminsk@gmail.com">travellabminsk@gmail.com</a><br/>
                                            <a class="mobile_link" href="http://www.travellab.by/?utm_source=email_distribution">travellab.by</a>
                                          </div>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <!-- greating -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="color:#FFFFFF;" bgcolor="#505882">
                    <tr>
                      <td align="center" valign="top">
                      <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                        <tr>
                          <td align="center" valign="top" width="500" class="flexibleContainerCell">
                            <table border="0" cellpadding="30" cellspacing="0" width="100%">
                              <tr>
                                <td align="center" valign="top" class="textContent">
                                  <h1 style="color:#FFFFFF;line-height:100%;font-family:Helvetica,Arial,sans-serif;font-size:35px;font-weight:normal;margin-bottom:5px;text-align:center;">Добрый день, уважаемые коллеги!</h1>
                                  <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#FFFFFF;line-height:135%;">Приглашаем Вас к совместной работе с нами!</div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <!-- advances -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#F8F8F8">
                    <tr>
                      <td align="center" valign="top">
                        <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td align="center" valign="top" width="500" class="flexibleContainerCell">
                              <table border="0" cellpadding="30" cellspacing="0" width="100%">
                                <tr>
                                  <td align="center" valign="top">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                      <tr>
                                        <td valign="top" class="textContent">
                                          <h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;">Преимущества сотрудничества с нами:</h3>
                                          <div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                            <ol>
                                              <li><strong>Гарантированные выезды</strong> - подтверждение этому является отсутствие отмененных выездов за время работы компании.</li>
                                              <li><strong>Профессионализм и опыт наших сотрудников</strong> - основа нашей компании.</li>
                                              <li><strong>Положительные эмоции</strong> - это то, что мы оставляем нашим туристам после поездки.</li>
                                              <li><strong>Лояльность</strong> - для наших постоянных партнеров предусмотрены специальные условия.</li>
                                            </ol>
                                          </div>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <!-- hr -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody>
                      <tr>
                        <td align="center" valign="top">
                          <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                            <tbody>
                              <tr>
                                <td align="center" valign="top" width="500" class="flexibleContainerCell">
                                  <table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
                                    <tbody>
                                      <tr>
                                        <td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">
                                          <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tbody>
                                              <tr>
                                                <td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <!-- tours -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody>
                      <tr>
                        <td align="center" valign="top">
                          <table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
                            <tbody>
                              <tr>
                                <td valign="top" width="500" class="flexibleContainerCell">
                                  <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tbody>
                                      <tr>
                                        <td align="left" valign="top" class="flexibleContainerBox">
                                          <table border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                            <tbody>
                                              <tr>
                                                <td align="left" class="textContent">
                                                  <a href="http://www.travellab.by/weekendlvov/?utm_source=email_distribution"><img src="cid:lvov" width="210" class="flexibleImage" style="max-width:100%;" alt="Тур во Львов" title="Тур во Львов"></a>
                                                  <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:10px;margin-bottom:3px;text-align:left;"><a href="http://www.travellab.by/weekendlvov/?utm_source=email_distribution">Тур во Львов</a></h3>
                                                  <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                                  Комиссия составляет:<br/>
                                                  20 BYN и 10% от 50$ - 5$.</div>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                        <td align="right" valign="middle" class="flexibleContainerBox">
                                          <table class="flexibleContainerBoxNext" border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                            <tbody>
                                              <tr>
                                                <td align="left" class="textContent">
                                                  <a href="http://www.travellab.by/karpati/?utm_source=email_distribution"><img src="cid:karpati" width="210" class="flexibleImage" style="max-width:100%;" alt="Тур в Карпаты" title="Тур в Карпаты"></a>
                                                  <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:10px;margin-bottom:3px;text-align:left;"><a href="http://www.travellab.by/karpati/?utm_source=email_distribution">Тур в Карпаты</a></h3>
                                                  <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                                  Комиссия составляет:<br/>
                                                  20 BYN и 10% от 85$ - 8,5$.</div>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <!-- hr -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody>
                      <tr>
                        <td align="center" valign="top">
                          <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                            <tbody>
                              <tr>
                                <td align="center" valign="top" width="500" class="flexibleContainerCell">
                                  <table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
                                    <tbody>
                                      <tr>
                                        <td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">
                                          <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tbody>
                                              <tr>
                                                <td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <!-- tours -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody>
                      <tr>
                        <td align="center" valign="top">
                          <table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
                            <tbody>
                              <tr>
                                <td valign="top" width="500" class="flexibleContainerCell">
                                  <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tbody>
                                      <tr>
                                        <td align="left" valign="top" class="flexibleContainerBox">
                                          <table border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                            <tbody>
                                              <tr>
                                                <td align="left" class="textContent">
                                                  <a href="http://www.travellab.by/weekendlvov2/?utm_source=email_distribution"><img src="cid:lvov_november" width="210" class="flexibleImage" style="max-width:100%;" alt="Тур во Львов ноябрьские праздиники" title="Тур во Львов ноябрьские праздиники"></a>
                                                  <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:10px;margin-bottom:3px;text-align:left;"><a href="http://www.travellab.by/weekendlvov2/?utm_source=email_distribution">Ноябрь во Львове</a></h3>
                                                  <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                                  Комиссия составляет:<br/>
                                                  20 BYN и 10% от 75$ - 7,5$.</div>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                        <td align="right" valign="middle" class="flexibleContainerBox">
                                          <table class="flexibleContainerBoxNext" border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                            <tbody>
                                              <tr>
                                                <td align="left" class="textContent">
                                                  <a href="http://www.travellab.by/lvov-new-year/?utm_source=email_distribution">
                                                    <img src="cid:lvov_new_year" width="210" class="flexibleImage" style="max-width:100%;" alt="Новый год во Львове" title="Новый год во Львове">
                                                  </a>
                                                  <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:10px;margin-bottom:3px;text-align:left;"><a href="http://www.travellab.by/lvov-new-year/?utm_source=email_distribution">Новый год во Львове</a></h3>
                                                  <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                                  Комиссия составляет:<br/>
                                                  20 BYN и 10% от 110$ - 11$.</div>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <!-- hr -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody>
                      <tr>
                        <td align="center" valign="top">
                          <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                            <tbody>
                              <tr>
                                <td align="center" valign="top" width="500" class="flexibleContainerCell">
                                  <table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
                                    <tbody>
                                      <tr>
                                        <td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">
                                          <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tbody>
                                              <tr>
                                                <td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <!-- tours -->
              <tr>
                <td align="center" valign="top">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody>
                      <tr>
                        <td align="center" valign="top">
                          <table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
                            <tbody>
                              <tr>
                                <td valign="top" width="500" class="flexibleContainerCell">
                                  <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tbody>
                                      <tr>
                                        <td align="left" valign="top" class="flexibleContainerBox">
                                          <table border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                            <tbody>
                                              <tr>
                                                <td align="left" class="textContent">
                                                  <a href="http://www.travellab.by/karpati-winter/?utm_source=email_distribution"><img src="cid:karpati_winter" width="210" class="flexibleImage" style="max-width:100%;" alt="Горнолыжный тур в Карпаты" title="Горнолыжный тур в Карпаты"></a>
                                                  <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:10px;margin-bottom:3px;text-align:left;"><a href="http://www.travellab.by/karpati-winter/?utm_source=email_distribution">Тур Горнолыжный тур в Карпаты</a></h3>
                                                  <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                                  Комиссия составляет:<br/>
                                                  20 BYN и 10% от 80$ - 8$.</div>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                        <td align="right" valign="middle" class="flexibleContainerBox">
                                          <table class="flexibleContainerBoxNext" border="0" cellpadding="0" cellspacing="0" width="210" style="max-width:100%;">
                                            <tbody>
                                              <tr>
                                                <td align="left" class="textContent">
                                                  <a href="http://www.travellab.by/new-year-spb/?utm_source=email_distribution"><img src="cid:new-year-spb" style="max-width:100%;" alt="Новый Год в Санкт-Петербурге" title="Новый Год в Санкт-Петербурге"></a>
                                                  <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:10px;margin-bottom:3px;text-align:left;"><a href="http://www.travellab.by/new-year-spb/?utm_source=email_distribution">Новый Год в Спб</a></h3>
                                                  <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">
                                                  Комиссия составляет:<br/>
                                                  20 BYN и 10% от 125$ - 12,5$.</div>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <!-- footer -->
              <table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailFooter">
                <tbody>
                  <tr>
                    <td align="center" valign="top">
                      <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tbody>
                          <tr>
                            <td align="center" valign="top">
                              <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                                <tbody>
                                  <tr>
                                    <td align="center" valign="top" width="500" class="flexibleContainerCell">
                                      <table border="0" cellpadding="30" cellspacing="0" width="100%">
                                        <tbody>
                                          <tr>
                                            <td valign="top" bgcolor="#E1E1E1">
                                              <div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
                                              <div>Copyright © 2017 <a href="http://www.travellab.by" target="_blank" style="text-decoration:none;color:#828282;"><span style="color:#828282;">Travel Lab</span></a>. Все права защищены.</div>
                                              </div>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
            </table>
          </td>
        </tr>
      </table>
    </center>
  </body>
</html>
    """
msg_text = MIMEText(html_txt, 'html')
msg_alternative.attach(msg_text)

with open('logo.jpg', 'rb') as img:
    msg_img_logo = MIMEImage(img.read())
msg_img_logo.add_header('Content-ID', '<logo>')
msg_root.attach(msg_img_logo)

with open('lvov.jpg', 'rb') as img:
    msg_img_lvov = MIMEImage(img.read())
msg_img_lvov.add_header('Content-ID', '<lvov>')
msg_root.attach(msg_img_lvov)

with open('karpati.jpg', 'rb') as img:
    msg_img_karpati = MIMEImage(img.read())
msg_img_karpati.add_header('Content-ID', '<karpati>')
msg_root.attach(msg_img_karpati)

with open('lvov_november.jpg', 'rb') as img:
    msg_img_lvov_november = MIMEImage(img.read())
msg_img_lvov_november.add_header('Content-ID', '<lvov_november>')
msg_root.attach(msg_img_lvov_november)

with open('lvov_new_year.jpg', 'rb') as img:
    msg_img_lvov_new_year = MIMEImage(img.read())
msg_img_lvov_new_year.add_header('Content-ID', '<lvov_new_year>')
msg_root.attach(msg_img_lvov_new_year)

with open('karpati_winter.jpg', 'rb') as img:
    msg_img_karpati_winter = MIMEImage(img.read())
msg_img_karpati_winter.add_header('Content-ID', '<karpati_winter>')
msg_root.attach(msg_img_karpati_winter)

with open('new-year-spb.jpg', 'rb') as img:
    msg_img_new_year_spb = MIMEImage(img.read())
msg_img_new_year_spb.add_header('Content-ID', '<new-year-spb>')
msg_root.attach(msg_img_new_year_spb)


try:
    email_conn = SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, msg_root.as_string()) 
    email_conn.quit()
    print("Message was sent")
except SMTPException: 
    print("Error occuer")
