while read hash; do
  curl -o images/$hash.jpg http://i.imgur.com/$hash.jpg
done <hashes.txt

# remove all 0 btye images
find ./images/ -size 0 -print0 | xargs -0 rm
