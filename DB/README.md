#### Xoa db cu: 
mongo
use TMDT;
db.dropDatabase();
exit;
#### restore db moi:
# mongorestore -d tmdt "/duong/dan/thu/muc/backup/nay"
