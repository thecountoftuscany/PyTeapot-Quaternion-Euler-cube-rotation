import os
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import argparse
from pyteapot import resizewin, init, draw

def visualize_quarternion_from_csv(file_path, useQuat, column_ids, delimiter, skip_header=True):
    video_flags = OPENGL | DOUBLEBUF
    pygame.init()
    screen = pygame.display.set_mode((640, 480), video_flags)
    pygame.display.set_caption("PyTeapot IMU orientation visualization")
    resizewin(640, 480)
    init()
    ticks = pygame.time.get_ticks()
    frames = 0
    
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            if(skip_header):
                skip_header = False
                continue
            if(useQuat):
                [w, nx, ny, nz] = [float(line.split(delimiter)[id]) for id in column_ids]
                draw(w, nx, ny, nz, useQuat)
            else:
                [yaw, pitch, roll] = [float(line.split(delimiter)[id]) for id in column_ids]
                draw(1, yaw, pitch, roll, useQuat)
            pygame.display.flip()
            frames += 1
    print("fps: %d" % ((frames*1000)/(pygame.time.get_ticks()-ticks)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--useQuat', type=bool, default=False, help='set true for using quaternions, false for using y,p,r angles')
    parser.add_argument('--text_file_path', type=str, default='data.csv', help='text file name')
    parser.add_argument('--delimiter', type=str, default=',', help='delimiter for file')
    parser.add_argument('--column_ids', type=str, default='1,2,3,4', help='quarternion/euler column indices in the file')
    args = parser.parse_args()

    useQuat = args.useQuat
    file_path = args.text_file_path
    delimiter = args.delimiter
    column_ids = [int(id) for id in args.column_ids.split(',')]
    if useQuat and len(column_ids) != 4:
        raise Exception('Quaternion column indices should be 4. Representing qw, qx, qy, qz respectively')
    if not useQuat and len(column_ids) != 3:
        raise Exception('Euler column indices should be 3. Representing yaw, pitch, roll respectively')

    if os.path.exists(file_path):
        visualize_quarternion_from_csv(file_path, useQuat, column_ids, delimiter, skip_header=True)
    else:
        raise FileNotFoundError('File not found: {}'.format(file_path))
