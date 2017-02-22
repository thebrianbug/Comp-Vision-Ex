import cv2
from matplotlib import pyplot as plt
a=cv2.imread('Ex5/dim.bmp', 0)
b=a*2+10
c=cv2.equalizeHist(a)
cv2.imwrite('Ex5/img_b.bmp',b)
cv2.imwrite('Ex5/img_c.bmp',c)
hist_a = cv2.calcHist([a],[0],None,[256],[0,256])
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])
hist_c = cv2.calcHist([c],[0],None,[256],[0,256])
#To avoid auto intensity adjustment, set vmin/vmax in plt.imshow
plt.subplot(321); plt.imshow(a, cmap='gray', vmin = 0, vmax = 255)
plt.subplot(322); plt.plot(hist_a);
plt.subplot(323); plt.imshow(b, cmap='gray', vmin = 0, vmax = 255)
plt.subplot(324); plt.plot(hist_b);
plt.subplot(325); plt.imshow(c, cmap='gray', vmin = 0, vmax = 255)
plt.subplot(326); plt.plot(hist_c);
plt.show()
