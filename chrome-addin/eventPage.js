var sendToLanraragi = {
	"id": "pAdd",
	"title": "Add Gallery to Lanraragi",
	"contexts": ["page"]
};
var sendToLanraragiLink = {
	"id": "pAddL",
	"title": "Add Gallery to Lanraragi",
	"contexts": ["link"]
};

chrome.contextMenus.create(sendToLanraragi);
chrome.contextMenus.create(sendToLanraragiLink);

function sendGallery(gid, gtkn) {
	fetch("http:YOURURLTOSERVER/archive.php?galID="+gid+"&galToken="+gtkn)
}

chrome.contextMenus.onClicked.addListener(function (clickData) {
	if(clickData.menuItemId == "pAdd" && clickData.pageUrl) {
		var urlP = clickData.pageUrl;
		urlP = urlP.substring(23);
		urlP = urlP.split("/");
		sendGallery(urlP[0],urlP[1]);
	}
	if(clickData.menuItemId == "pAddL" && clickData.linkUrl) {
		var urlP = clickData.linkUrl;
		urlP = urlP.substring(23);
		urlP = urlP.split("/");
		sendGallery(urlP[0],urlP[1]);		
	}
});