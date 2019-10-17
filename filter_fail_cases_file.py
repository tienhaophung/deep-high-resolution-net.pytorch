import json

score_thresh = 0.9

def filter_fail_cases(file_name_input, file_name_output):
    with open(file_name_input) as f:
        # Load json files
        results = json.load(f)

        count = 0

        fout = open(file_name_output, "wt")
        # Loop over results list
        for result in results:
            if result['score'] > score_thresh:
                fout.write(str(result["image_id"]).rjust(12, '0'))
                fout.write('\n')
                count += 1

        print("Number of fail cases:", count)
        print("Number of total cases:", len(results))

        fout.close()

file_name_input = '/Users/haophung/Google Drive (brianphungai@gmail.com)/deep-high-resolution-net.pytorch/output/coco/pose_hrnet/w48_384x288_adam_lr1e-3/val2017/results/keypoints_val2017_results_0.json'
file_name_output = "coco_fail_cases.txt"
