from segment_class import Segmenter
#import Segmenter
#初始化的时候先读入了停用词
segmenter = Segmenter()
segmenter.read_dir_name()
segmenter.segment(fq=0)
