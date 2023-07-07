<?php
    function queryPanda($galID,$tokenID) {
            $providerAPI = "https://exhentai.org/api.php";
            $galleryQuery = array(
                "method" => "gdata",
                "gidlist" => array(array($galID,$tokenID)),
                "namespace" => 1	
            );
            $payload = json_encode($galleryQuery);
            $ch=curl_init($providerAPI);
            curl_setopt($ch, CURLOPT_POST, 1);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Accept:application/jsonrequest'));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
            $result = curl_exec($ch);
            curl_close($ch);
            return json_decode($result, true);
    }
	function downloadArchive($gid, $gtoken, $atoken) {
		$url = 'https://exhentai.org/archiver.php?gid='.$gid.'&token='.$gtoken.'&or='.$atoken;
		$cookie1 = 'ipb_pass_hash=YOUR PASS HASH HERE';
		$cookie2 = 'ipb_member_id=YOUR MEMBER ID HERE';
		$data = array(
		  'dltype' => 'res', //this can be set to res for the resample or to org for the original(more hath cost)
		  'dlcheck' => 'Download Resample Archive' //Set to "Download Resample Archive" or "Download Original Archive".
		);
		$ch = curl_init($url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_COOKIE, $cookie1 . '; ' . $cookie2);
		curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
		curl_setopt($ch, CURLOPT_HEADER, true);
		$response = curl_exec($ch);
		if ($response === false) {
			$error = curl_error($ch);
		}
		$redirectURL = "";
		if (preg_match('/document.location\s*=\s*"([^"]+)";/', $response, $matches)) {
		  $url = $matches[1];
		  
		  $redirectURL = $url;
		} else {
		  echo "URL not found";
		}	
		return $redirectURL.'?start=1';
	}
?>