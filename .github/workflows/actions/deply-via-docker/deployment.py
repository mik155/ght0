import os


def run():
    bucket = os.environ['INPUT_BUCKET']
    bucket_region = os.environ['INPUT_REGION']
    dist_folder = os.environ['INPUT_FOLDER']

    print(f'Bucket: {bucket}')
    print(f'Region: {bucket_region}')
    print(f'Folder: {dist_folder}')

    website_url = 'www.google.com'
    # The below code sets the 'website-url' output (the old ::set-output syntax isn't supported anymore - that's the only thing that changed though)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'website-url={website_url}', file=gh_output)


if __name__ == '__main__':
    run()
