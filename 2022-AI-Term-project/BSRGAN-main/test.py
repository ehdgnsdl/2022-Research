import torch
import cv2
import os
from utils import utils_image as util
from models.network_rrdbnet import RRDBNet as net

# https://github.com/cszn/KAIR/releases/download/v1.0/BSRGAN.pth
# `model_zoo/BSRGAN.pth`
sum = 0

for i in range(433):    
    #image 입력
    img_path = 'result/Cars' + str(i) + '.png'

    # 모델 load
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    #print(device)

    # BSRGAN에 관련된 논문을 보면 좋을 듯함.
    model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=4)
    model.load_state_dict(torch.load(os.path.join('model_zoo', 'BSRGAN.pth')), strict=True)
    model = model.to(device)
    model.eval()

    with torch.no_grad():
        # image를 load
        img = cv2.imread(img_path)
        # 3채널로 변경
        img_L = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        # tensor형태로 바꿔주고
        img_L = util.uint2tensor4(img_L)
        # GPU or CPU 사용
        img_L = img_L.to(device)

        img_E = model(img_L)

        # 다시 img로 변환
        img_E = util.tensor2uint(img_E)
        # img를 저장
        util.imsave(img_E, os.path.splitext(img_path)[0] + '.png')
        sum += 1

print(sum)