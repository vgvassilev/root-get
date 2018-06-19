import wget
import urllib2
from git import Repo
import re

class Downloader_request(object):
    """Constructor for Downloader_request."""
    def __init__(self, url, dir):
        super(Downloader_request, self).__init__()
        self.url = url
        self.dir = dir

    # FIXME: next step is to move to PyGithub
    def download_github(self):
        repository = re.findall(r'/(\w+)', self.url)[-1]
        print("We would like to download {0:s}".format(repository))
        git_directory = self.dir + "/" + repository
        Repo.clone_from(self.url, git_directory)
        print("Cloning from github %s", self.url)

    # FIXME: non finished routine
    def download_zip(self):
        wget.download(self.url, self.dir)
        print("Downloading from http/https %s", self.url)

    def resolving_download(self):
        request = urllib2.Request(self.url)
        request.get_method = lambda : 'HEAD'
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            return False
        # check if we have github link
        match = re.search('github', self.url)
        if match:
            self.download_github()
        else:
            self.download_zip()
