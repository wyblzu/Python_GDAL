__author__ = 'wyb'
# -*- coding:utf-8 -*-
# testing gdal-lib
import gdal
import numpy
import struct
from gdalconst import *
dataset = gdal.Open('/home/wyb/data/SPOT.img', GA_ReadOnly)
if dataset is None:
    print 'Nodata'
else:
    print 'Driver:', dataset.GetDriver().ShortName, '/', \
        dataset.GetDriver().LongName
    print 'Size is', dataset.RasterXSize, 'x', dataset.RasterYSize,\
        'x', dataset.RasterCount
    print 'Projection is', dataset.GetProjection()
geotransform = dataset.GetGeoTransform()
if not geotransform is None:
    print 'Origin = (', geotransform[0], ',', geotransform[3], ')'
    print 'Pixel Size = (', geotransform[1], ',', geotransform[5], ')'
    print 'Angle = (', geotransform[2], ',', geotransform[4], ')'
band = dataset.GetRasterBand(1)
print 'Band Type = ', gdal.GetDataTypeName(band.DataType)

min = band.GetMinimum()
max = band.GetMaximum()
if min is None or max is None:
    (min, max) = band.ComputeRasterMinMax(1)
print 'min = %.3f, max = %.3f' % (min, max)
if band.GetOverviewCount() > 0:
    print 'Band has ', band.GetOverviewCount(), ' overviews.'
if not band.GetRasterColorTable() is None:
    print 'Band has  a color table with ', band.GetRasterColorTable().GetCount(), ' entries.'
scanline = band.ReadRaster(0, 0, band.XSize, 1, band.XSize, 1, GDT_Float32)
tuple_of_floats = struct.unpack('f' * band.XSize, scanline)
print tuple_of_floats

# qwer = dataset.G
# width = dataset.RasterXSize
# height = dataset.RasterYSize
# bw = 0.1
# bh = 0.1
# x = int(width*bw)
# y = int(height*bh)
# datas = []
# for i in range(3):
#     band = dataset.GetRasterBand(i + 1)
#     data = band.ReadAsArray(0, 0, width, height, x, y)
#     datas.append(numpy.reshape(data, (1, -1)))
# datas = numpy.concatenate(datas)
# driver = gdal.GetDriverByName("GTiff")
# tods = driver.Create('/home/wyb/pycharm/data/tpix2.tiff', x, y, 3, options=["INTERLEAVE=PIXEL"])
# tods.WriteRaster(0, 0, x, y, datas.tostring(), x, y, band_list=[1, 2, 3])


    # import gdal
    # import numpy
    # from gdalconst import *
    # dataset = gdal.Open("aster//earth.img")
    # width = dataset.RasterXSize
    # height = dataset.RasterYSize
    # bw = 0.1
    # bh = 0.1
    # x = int(width*bw)
    # y = int(height*bh)
    # datas = []
    # for i in range(3):
    #     band = dataset.GetRasterBand(i+1)
    #     data = band.ReadAsArray(0,0,width,height,x,y)
    #     datas.append(numpy.reshape(data,(1,-1)))
    # datas = numpy.concatenate(datas)
    # driver = gdal.GetDriverByName("GTiff")
    # tods = driver.Create("Raster//tpix1.tif",x,y,3,options=["INTERLEAVE=PIXEL"])
    # tods.WriteRaster(0,0,x,y,datas.tostring(),x,y,band_list=[1,2,3])



#test
