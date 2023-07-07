<?php
	ini_set('memory_limit', '4096M');
	require_once('panda.php');
	$galID = $_GET['galID'];
	$galToken = $_GET['galToken'];

	if ($galID and $galToken) {
		$galMeta = queryPanda($galID,$galToken);
		$galleryName = $galMeta['gmetadata'][0]['title'];
		$galArchiveToken = $galMeta['gmetadata'][0]['archiver_key'];
		$cleanedName = preg_replace('/[^\p{L}\p{N}\s-]/u', '', $galleryName);
		$cleanedName = trim($cleanedName);
		$cleanedName = preg_replace('/\s+/', ' ', $cleanedName);
		$cleanedName = str_replace(' ', '_', $cleanedName);		
		$archiveUrl = downloadArchive($galID, $galToken, $galArchiveToken);
		$fileContent = file_get_contents($archiveUrl);
		mkdir('./downloads/'.$galID.'-'.$galToken, 0777);
		file_put_contents('./downloads/'.$galID.'-'.$galToken.'/'.$cleanedName.'.zip', $fileContent);		
	}
?>