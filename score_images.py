import os
import csv
import subprocess

with open('results.csv','w') as results:
    results = csv.writer(results, delimiter=',')

    results.writerow(['hash', 'score'])

    for hash in open('hashes.txt'):
        hash = hash.strip()
        print '=== starting on ' + hash

        filename = "images/%s.jpg" % hash

        if not os.path.isfile(filename):
            results.writerow([hash, 'invalid'])
            print '%s - invalid' % hash
            continue

        FNULL = open(os.devnull, 'w')
        try:
            result = subprocess.Popen("docker run --volume=$(pwd):/workspace caffe:cpu python ./classify_nsfw.py --model_def nsfw_model/deploy.prototxt --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel images/%s.jpg" % hash, stderr=FNULL, stdout=subprocess.PIPE, shell=True).stdout.read().split(' ')[4].strip()
        except IndexError:
            results.writerow([hash, 'error'])
            print '%s - %s' % (hash, 'error')
            continue

        print '%s - %s' % (hash, result)

        results.writerow([hash, result])
