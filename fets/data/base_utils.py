import os 

# FIXME: Look to all usages and fix the fact that we are inspecting files multiple times
#  for example we can optimize how we determine which patient directories to exlcude due to missing files 
def get_appropriate_file_paths_from_subject_dir(dir_path):
    '''
    This function takes a subject directory as input and return a dictionary of the full paths to the modalities (BraTS-specific)
    '''
    filesInDir = os.listdir(dir_path)

    returnDict = {}

    # FIXME: There is more than one place the list below is defined
    # Move to one location and ensure sync with feature_modes from the flplan
    brats_modalities = ['T1', 'T2', 'FLAIR', 'T1CE']
    for mod in brats_modalities:
      returnDict[mod] = None

    # get the input image files and ground truth
    for i in range(len(filesInDir)):
        currentFile = os.path.abspath(os.path.join(dir_path,filesInDir[i]))
        if filesInDir[i].endswith('_t1ce.nii.gz'):
            if returnDict['T1CE'] is None:
                returnDict['T1CE'] = currentFile
            else:
                print('WARNING: T1CE file found before, something is going haywire with the files in this directory: ', dir_path)
        elif filesInDir[i].endswith('_t1gd.nii.gz'):
            if returnDict['T1CE'] is None:
                returnDict['T1CE'] = currentFile
            else:
                print('WARNING: T1CE file found before, something is going haywire with the files in this directory: ', dir_path)
        elif filesInDir[i].endswith('_flair.nii.gz'):
            if returnDict['FLAIR'] is None:
                returnDict['FLAIR'] = currentFile
            else:
                print('WARNING: FLAIR file found before, something is going haywire with the files in this directory: ', dir_path)
        elif filesInDir[i].endswith('_t1.nii.gz'):
            if returnDict['T1'] is None:
                returnDict['T1'] = currentFile
            else:
                print('WARNING: T1 file found before, something is going haywire with the files in this directory: ', dir_path)
        elif filesInDir[i].endswith('_t2.nii.gz'):
            if returnDict['T2'] is None:
                returnDict['T2'] = currentFile
            else:
                print('WARNING: T2 file found before, something is going haywire with the files in this directory: ', dir_path)

    return returnDict
