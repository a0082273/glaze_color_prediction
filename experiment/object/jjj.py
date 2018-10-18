#!/usr/local/bin/python
#! -*- coding: utf-8 -*-

#https://qiita.com/neriai/items/448a36992e308f4cabe2

import cv2
import numpy as np

# 指定した画像(path)の物体を検出し、外接矩形の画像を出力します
def detect_contour(path):

  # 画像を読込
  src = cv2.imread(path, cv2.IMREAD_COLOR)

  height, width, channels = src.shape
  size = height * width

  # グレースケール画像へ変換
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

  # ぼかす
  # blur = cv2.blur(gray, (5,5))

  # 2値化
  # retval, bw = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  # retval, bw = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  # retval, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  retval, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

  # 輪郭を抽出
  # image, contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  # image, contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  image, contours, hierarchy = cv2.findContours(bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # 矩形検出された数（デフォルトで0を指定）
  detect_count = 0

  # 各輪郭に対する処理
  outputs = []
  rects = []
  approxes = []

  for i in range(len(contours)):

    # 輪郭の領域を計算
    area = cv2.contourArea(contours[i])

    # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
    if area < size*0.1 or size*0.99 < area:
      continue

    # 外接矩形
    if len(contours[i]) > 0:


      cnt = contours[i]
      arclen = cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, 0.02*arclen, True)
      if len(approx) < 4:
        continue
      approxes.append(approx)
      rect = getRectByPoints(approx)
      rects.append(rect)
      outputs.append(getPartImageByRect(rect))
      cv2.imwrite('output/'+str(i)+'.jpg', getPartImageByRect(rect))

      # rect = contours[i]
      # x, y, w, h = cv2.boundingRect(rect)
      # cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

      # # 外接矩形毎に画像を保存
      # cv2.imwrite(path[:-4] + '_' + str(detect_count) + '.jpg', src[y:y + h, x:x + w])

      detect_count = detect_count + 1


  # 外接矩形された画像を表示
  cv2.imshow('output', src)
  cv2.waitKey(0)

  # 終了処理
  cv2.destroyAllWindows()


def getRectByPoints(points):
    # prepare simple array
    points = list(map(lambda x: x[0], points))

    points = sorted(points, key=lambda x:x[1])
    top_points = sorted(points[:2], key=lambda x:x[0])
    bottom_points = sorted(points[2:4], key=lambda x:x[0])
    points = top_points + bottom_points

    left = min(points[0][0], points[2][0])
    right = max(points[1][0], points[3][0])
    top = min(points[0][1], points[1][1])
    bottom = max(points[2][1], points[3][1])
    return (top, bottom, left, right)

def getPartImageByRect(rect):
    img = cv2.imread(path, 1)
    return img[rect[0]:rect[1], rect[2]:rect[3]]


if __name__ == '__main__':
  # path = 'tile_scan2.jpg'
  # path = 'IMG_20181017_114345.jpg'
  path = 'IMG_20181017_140437_2.jpg'
  detect_contour(path)
