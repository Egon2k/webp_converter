from PIL import Image
import sys, os

converted_folder =  'converted'             # folder where webps will be moved after conversion - keep empty to delete

for i in range(len(sys.argv) - 1):
    if sys.argv[i + 1].endswith('.webp'):
        webp_path = sys.argv[i + 1]
        webp_fold = '/'.join(webp_path.split('\\')[:-1])
        webp_file = webp_path.split('\\')[-1]
        jpeg_path = webp_path.split('.')[-2] + '.jpg'
        
        if i == 0 and converted_folder != '':
            # make directory for converted files
            cmd = f'mkdir "{webp_fold}/{converted_folder}"'
            os.system(cmd)        
        
        print('=== convert ' + webp_file)
        
        # open webp and save as jpg
        im = Image.open(webp_path).convert('RGB')
        im.save(jpeg_path, 'jpeg')
        
        if converted_folder != '':
            # move webp file to converted folder
            cmd = f'move "{webp_path}" "{webp_fold}/{converted_folder}/{webp_file}"'
            os.system(cmd)
        else:
            # delete webp file
            cmd = f'del "{webp_file}"'
            os.system(cmd)
