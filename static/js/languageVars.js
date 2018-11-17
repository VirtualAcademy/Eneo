var lang=0;
//guess the language of the user by the browser language set.  If the user selects a different language this is overridden.
var languageGuess = window.navigator.userLanguage || window.navigator.language;

if (languageGuess.indexOf("es") > -1) {
    lang=2;
  } else if (languageGuess.indexOf("fr") > -1) {
    lang=1;
  } else {
    lang=0;
}


var urlParams;
(window.onpopstate = function () {
    var match,
        pl     = /\+/g,  // Regex for replacing addition symbol with a space
        search = /([^&=]+)=?([^&]*)/g,
        decode = function (s) { return decodeURIComponent(s.replace(pl, " ")); },
        query  = window.location.search.substring(1);

    urlParams = {};
    while (match = search.exec(query))
       urlParams[decode(match[1])] = decode(match[2]);
})();


if(urlParams["lang"] != undefined){
  lang=urlParams["lang"];
}

var SustainableInternetAccessSystem  = ["Fuel Monitoring and Management System","Syst�me de Gestion et du � Monitoring d'Essence"];

//language settings in user login
var UserLogin=["User Login","Connexion"];
var Areyouloggedin = ["Are you logged in?","�tes-vous connect� �?"];
var Ifnot=["If not,","Si non,"];
var ClickHere = ["Click Here","Cliquez Ici"];
var ClickHeretogotothemainportalfree = ["Click Here to go to the main portal (free!)","Cliquez ici pour aller sur le portail principal (gratuit!)"];
var MainPortal = ["Main Portal","Portail Principal"];
var OrPressF5KeyToRefresh=["--Or press F5 key to refresh--","--Ou appuyez sur la touche F5 pour actualiser--"];

var YouhaveLoggedIn = ["You have Logged In", "Vous �tes connect�"];
var Pleasekeep = ["Please keep this window open and remember to logout when finished","S'il vous pla�t garder cette fen�tre ouverte et n'oubliez pas de vous d�connecter lorsque vous avez termin�"];
var Hello = ["Hello","Bonjour"];
var StartTime = ["Start Time", "Heure de d�but"];
var Duration = ["Duration", "Dur�e"];
var BytesTransferred = ["Bytes Transferred (Download+Upload)","Octets transf�r�s (t�l�chargement+t�l�charger)","Bytes transferidos (Descargar+Subir)"];
var Rate = ["Rate","Tarif","Tarifa"];
var Bill = ["Bill","Facture","Factura"];
var Refresh = ["Refresh","Rafra�chir","Actualizaci�n"];
var Logout = ["logout","d�connexion","cerrar sesi�n"];
var Login = ["login","connexion","iniciar sesi�n"];
var PleaseDoNot = ["Please do not accept your browser's option to store your password.  Other people can steal your credit if you do this.","N'acceptez pas l'option de votre navigateur pour enregistrer votre mot de passe. D'autres personnes peuvent voler votre cr�dit si vous faites cela.","No acepte la opci�n de su navegador para almacenar su contrase�a. Otras personas pueden robar su cr�dito si lo hace."];

var ThisfacilityoffersInternetaccess = ["This facility offers Internet access for personal/work use. To use this connection, please signup at <a href=Signuplocation.png>your institution</a>. Internet may be billed on data transferred or time online. Once you receive your username and password, please click the link below to login.","Cet �tablissement offre un acc�s Internet pour un usage personnel/travail. Pour utiliser cette connexion, s'il vous pla�t payer au <a href=Signuplocation.png>votre institution</a>. Internet est factur� sur une base de temps ou des donn�es transf�r�es. Une fois que vous recevez votre nom d'utilisateur et mot de passe, s'il vous pla�t cliquez sur le lien ci-dessous pour vous identifier.","Este servicio ofrece acceso a Internet para el uso / trabajo personal. Para utilizar esta conexi�n, por favor, preste en <a href=Signuplocation.png>su instituci�n</a>. Internet se factura en funci�n del tiempo o datos transferidos. Una vez que reciba su nombre de usuario y contrase�a, por favor haga clic en el enlace de abajo para iniciar sesi�n."];
var Remembertokeepthiswindow = ["Remember to keep this window open and 'Logout' when you are finished to prevent using up all your credit.<br><br>If you see a blue circle with a check in it here:","N'oubliez pas de garder cette fen�tre ouverte et 'D�connexion' lorsque vous avez termin� pour �viter d'utiliser tous votre cr�dit.<br><br>Si vous voyez un cercle bleu avec un ch�que ici:","Recuerde que debe mantener esta ventana abierta y 'Finalizar' cuando haya terminado para evitar el uso de todo su cr�dito.<br><br>Si usted ve un c�rculo azul con un cheque por aqu�:"];
var ThentheInternetconnection = ["Then your institution's Internet connection is currently working","Ensuite, la connexion Internet","Entonces la conexi�n a Internet est� trabajando actualmente"];
var MainPortal = ["Main Portal","Portail Accueil","Portal Principal"];
var MemberArea = ["Member Area","Espace Membres","Zona Miembro"];
var AssistantLogin = ["Assistant Login","Login Assistant","Acceso Asistente"];
var AdministratorLogin = ["Administrator Login","Login Administrateur","Acceso Al Administrador"];

var UserName = ["User Name","Nom d'utilisateur","Nombre de Usuario"];
var Password = ["Password","Mot de Passe","Contrase�a"];
var back = ["back","retour","retorno"];

var LoginFirst = ["Login First","Connectez-vous d'abord","Ingresar Primera"];

var YouhaveLoggedOut = ["You have Logged Out", "Vous vous �tes D�connect�", "Ha cerrado la sesi�n"];
var Thankyouforusingourservice  = ["Thank you for using our service","Merci d'utiliser notre service","Gracias por usar nuestros servicios"];
var Pleasecloseyourbrowser = ["Please close your browser to finish your logout.  ","S'il vous pla�t fermer votre navigateur pour terminer votre d�connexion.  ","Por favor, cierre su navegador para terminar su sesi�n.  "];
var Thankyou  = ["Thank you","Merci","Gracias"];
var EndTime  = ["End Time","Heure de fin","Hora de finalizaci�n"];
var TariffClass  = ["Billed By","Factur� Par","Facturado por"];
var TotalCreditUsedThisSession  = ["Total Credit Used This Session","Cr�dit total utilis� Cette session","Cr�dito total utilizado esta Sesi�n"];
var CheckActivity  = ["Check Activity","V�rifiez activit�","Comprobar Actividad"];
var OutOfCredit = ["Out of Credit?", "Cr�dit Fini?", "�Sin Cr�dito?"];
var IfYouAreSeeingThisForTheFirstTime = ["If you are seeing this for the first time, you may be out of credit. To check","Si vous voyez ce pour la premi�re fois, vous pouvez �tre hors de cr�dit. V�rifier","Si usted est� viendo esto por primera vez, usted puede estar fuera del cr�dito. Verificar"];
var ViewCredit = ["View Credit", "Vue Cr�dit", "Vista Cr�dito"];
var ViewYourMACAddress = ["View Your MAC Address","Voir Votre MAC","Ver su MAC"];
var IncorrectUsernameOrPassword = ["Incorrect username or password","identifiant ou mot de passe incorrect","Nombre de usuario o contrase�a incorrecta"];
var YourAccountIsAdministrativelyDisabled = ["Your account is administratively disabled","Votre compte est administrativement d�sactiv�","Su cuenta est� deshabilitada administrativamente"];

//Check Credit Page
var CheckAccountCreditUsage = ["Check Account Credit Usage", "V�rifiez L'utilisation Du Cr�dit Pour Votre Compte","Comprobar El Uso De Cr�dito Para Su Cuenta"];
var ClickTheButtonBelow = ["Click the button below to have the system search for your account based on the device you are using to access this page.","Cliquez sur le bouton ci-dessous pour avoir la recherche de syst�me pour votre compte en fonction de l'appareil que vous utilisez pour acc�der � cette page.","Haga clic en el bot�n de abajo para tener el sistema de b�squeda por su cuenta en funci�n del dispositivo que est� utilizando para acceder a esta p�gina."];
var AutomaticLookup = ["automatic lookup","automatique recherche","b�squeda autom�tica"];
var ManualLookup = ["Manual Lookup","Recherche Manuelle","B�squeda Manual"];
var EnterYourAccountNumber = ["Enter your account number below (often your phone number or badge number).","Entrez votre num�ro de compte ci-dessous (souvent votre num�ro de t�l�phone ou num�ro de badge).","Introduzca su n�mero de cuenta a continuaci�n (a menudo su n�mero de tel�fono o n�mero de placa)."];
var AccountNumber = ["Account Number","Num�ro de Compte","N�mero de Cuenta"];
var Submit = ["submit","rendre","entregar"];
var Return  = ["Return","Retourner","Volver"];
var AutomaticLookupReturnedAnInvalidIPAddress = ["Automatic Lookup returned an invalid IP Address.  Try looking up your account by your account number.","Automatique de recherche a retourn� une adresse IP non valide. Essayez de regarder votre compte par votre num�ro de compte.","Autom�tico de b�squeda devuelve una direcci�n IP no v�lida. Intente buscar por su cuenta su n�mero de cuenta."];
var AutomaticLookupCouldNotGather = ["Automatic Lookup could not gather the information necessary to look up your account.  Try looking up your account by your Username.","Automatique de recherche n'a pas pu recueillir les informations n�cessaires pour consulter votre compte. Essayez de regarder votre compte par votre nom d'utilisateur.","Operaciones de b�squeda autom�tica no pudo reunir la informaci�n necesaria para buscar su cuenta. Intente buscar por su cuenta nombre de usuario."];
var ViewYourCredit  = ["View Your Credit","Voir Votre Cr�dit","Ver su cr�dito"];
var ThisTableShows = ["This table shows how much data you have left on your account.  Your account includes all the data that was transferred to and from all your devices (such as laptops, tablets and phones).  This number includes uploads and downloads.  If your account is not enabled, please check in with IT as it has been administratively disabled.","Ce tableau montre la quantit� de donn�es que vous avez laiss� sur votre compte. Votre compte comprend toutes les donn�es qui ont �t� transf�r�es vers et depuis tous vos appareils (tels que les ordinateurs portables, tablettes et t�l�phones). Ce nombre inclut les t�l�chargements et les t�l�chargements. Si votre compte est pas activ�, s'il vous pla�t v�rifier avec l'informatique comme il a �t� d�sactiv� administrativement.","Esta tabla muestra la cantidad de datos que le queda en su cuenta. Su cuenta incluye todos los datos que se transfieren hacia y desde todos tus dispositivos (tales como ordenadores port�tiles, tabletas y tel�fonos). Este n�mero incluye las cargas y descargas. Si su cuenta no est� habilitada, por favor verificar con �l, ya que se ha deshabilitado administrativamente."];
var PersonalCredit  = ["Personal Credit","Cr�dit Personnel","Cr�dito Personal"];
var GivenCredit  = ["Given Credit","Cr�dit Donn�","Dado Cr�dito"];
var Enabled  = ["Enabled","Activ�e","Habilitado"];
var NoCustomerFoundWithThat = ["No customer found with that account number.","Aucun client trouv� avec ce num�ro de compte.","No se han encontrado con n�mero de cuenta del cliente."];
var ShowRecentActivity  = ["show recent activity","afficher activit� r�cente","mostrar la actividad reciente"];
var RecentActivityReport  = ["Recent Activity Report","R�cent Rapport D'activit�","Informe de Actividad Reciente"];
var Description  = ["Description","Description","Descripci�n"];
var MACAddress  = ["MAC Address","Adresse Mac","Direcci�n MAC"];
var LastFourOfMACAddress  = ["Last 4 of MAC Address","Dernier 4 de l'Adresse Mac","�ltimos 4 de la Direcci�n MAC"];
var DataUsedLastTenMinutes  = ["Data Used<br>Last 10 Minutes","Donn�es Utilis�es 10 Derni�res Minutes","Datos Utilizados Ultimos 10 Minutos"];
var DataUsedLastSixtyMinutes  = ["Data Used<br>Last 60 Minutes","Donn�es Utilis�es 60 Derni�res Minutes","Datos Utilizados Ultimos 60 Minutos"];
var DataUsedLastTwentyFourHours  = ["Data Used<br>Last 24 Hours","Donn�es Utilis�es 24 Derni�res Heures","Datos Utilizados Ultimos 24 Horas"];
var LastTwentyFourHoursActivityForAllDevicesOfThisCustomer  = ["Last 24 Hours Activity for all Devices of this Customer","Derni�re activit� 24 heures pour tous les appareils de ce client","�ltimas 24 horas de actividad para todos los dispositivos de este cliente"];
var LastMonthsActivityforallDevicesofthisCustomer  = ["Last Month's Activity for all Devices of this Customer","Activit� du mois dernier pour tous les appareils de ce client","Actividad del �ltimo mes para todos los dispositivos de este cliente"];
var MegabytesPerDay  = ["Megabytes / Day","M�gaoctets / Jour","Megabytes / D�a"];
var MegabytesPerFifteenMinutes = ["Megabytes per 15 minutes","M�gaoctets par 15 minutes","Megabytes por 15 minutos"];
var AverageKilobytesPerSecond  = ["Avg Kilobytes / Sec","Moyenne Kilooctets / Sec","Kilobytes Promedio / Segundo"];
var DText  = ["Date","La Date","La Fecha"];

//Get Mac Address
var TheMACAddressOfYourDeviceIs  = ["The MAC address of your device is:","L'adresse MAC de votre appareil est:","La direcci�n MAC de su dispositivo es:"];
var WeCouldNotFindYourMacAddress  = ["We could not find your mac address.  You may need to have your system administrator enable the following option in IPFIRE: Network -> Webproxy -> Client IP address forwarding","Nous ne pouvions pas trouver votre adresse mac. Vous devrez peut-�tre demander � votre administrateur syst�me d'activer l'option suivante dans IPFIRE: Network -> Webproxy -> Client IP address forwarding","No pudimos encontrar la direcci�n MAC. Es posible que deba tener el administrador del sistema habilitar la siguiente opci�n en IPFIRE: Network -> Webproxy -> Client IP address forwarding"];
var FailedPleaseTryAgainLater = ["Failed...Please try again later.<br><br>The System Administrator may need to restart squid<br><br>","�chec ... S'il vous pla�t r�essayer plus tard. <br> L'administrateur syst�me peut avoir besoin de red�marrer Squid<br><br>","No se pudo ... Por favor, int�ntelo de nuevo m�s tarde. <br> El administrador del sistema puede que tenga que reiniciar Squid<br><br>"];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];



//language settings in member preferences
var UserPortal  = ["User Portal","Portail de l'utilisateur","Portal del Usuario"];
var YourAccount  = ["Your Account","Votre Compte","Su Cuenta"];
var FullName  = ["Full Name","Nom et Pr�nom","Nombre Completo"];
var PasswordConfirm = ["Password (Confirm)","Mot de Passe (Confirmation)","Contrase�a (Confirmar)"];
var CreditRemaining  = ["Credit Remaining","Cr�dit Restant","Cr�dito Restante"];
var Payment  = ["Payment","Paiement","Pago"];
var Status  = ["Status","Statut","Estado"];
var YourUsage  = ["Your Usage","Votre Utilisation","Su Uso"];
var DateFrom  = ["Date, From :","Date, � Partir de:","Fecha, De:"];
var MemberName  = ["Member Name","Nom du Membre","Nombre de Usuario"];
var TotalUsage  = ["Total Usage","Utilisation Totale","Uso Total"];
var TotalBill  = ["Total Bill","Facture Totale","Factura Total"];
var Save  = ["Save","Enregistrer","Guardar"];

var January  = ["January","Janvier","Enero"];
var February  = ["February","F�vrier","Febrero"];
var March  = ["March","Mars","Marzo"];
var April  = ["April","Avril","Abril"];
var May  = ["May","Mai","Mayo"];
var June  = ["June","Juin","Junio"];
var July  = ["July","Juillet","Julio"];
var August  = ["August","Ao�t","Agosto"];
var September  = ["September","Septembre","Septiembre"];
var October  = ["October","Octobre","Octubre"];
var November  = ["November","Novembre","Noviembre"];
var December  = ["December","D�cembre","Diciembre"];

var to  = ["to","�","a"];
var Month  = ["Month","Mois","Mes"];
var Year  = ["Year","Ann�e","A�o"];

var yyyymmdd  = ["yyyy-mm-dd","aaaa-mm-jj","aaaa-mm-dd"];

var View  = ["View","Voir","Mirar"];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
var temp  = ["","",""];
