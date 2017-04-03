# exiffind
Find images by their exif tags'

# Install
```
$ pip3 install exiffind
```

# Usage
```bash
$ exiffind --ext jpg --after 2016-01-01 --before 2017-03-18 --author kormarun \
    --software gimp --orientation horizontal /path/to/images
    
/path/to/images/a.jpg
/path/to/images/deeper/b.jpg
```

```python
from exiffind import check
check({
    "dir":"",
    "after":"2016-01-01"
})
```