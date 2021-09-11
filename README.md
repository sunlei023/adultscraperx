# adultscraperx

#### [English](README.md) [简体中文](README-cn.md)

##### AdultScraperX is a porn video metadata scraper for the Gsetant platform, which can realize the matching and metadata acquisition of various resources such as Japanese censored, Japanese uncensored, animation and American resources. Gsetant can be automatically installed through this project address on the administrator plug-in management page https://github.com/sunlei023/adultscraperx

### Storage requirements and service configuration for local files

##### Due to the phenomenon of number conflicts between multiple movies, this plugin requires Japanese censored, Japanese uncensored, Japanese animation and American resources to be stored separately according to certain rules. The specific rules are as follows

##### Set the directory mark in the AdultScraperX plugin settings on the Gsetant server:
- The catalog marks of America and Japan (censored, uncensored, anime) can be customized in the plugin:
- Configure the home directory mark, which must contain (before and after) special characters such as: -M-, \*M\*, =M= and so on
- The directory mark can only appear once, and is consistent with the mark of the main directory folder name to be recognized

##### Examples of local home directory configuration flags:
- Modify your local folder as follows:
- volume1/japanese censored=M=/(numerous subdirectories)/(numerous files).mp4
- volume1/japanese uncensored=NM=/(numerous subdirectories)/(numerous files).mp4
- volume1/anime=A=/(numerous subdirectories)/(numerous files).mp4
- volume1/America=E=/(numerous subdirectories)/(numerous files).mp4
