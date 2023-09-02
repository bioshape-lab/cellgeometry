import numpy as np
from skimage.morphology import label
import SimpleITK as sitk
from celldataset import IndexTracker, IndexTracker2

# from matplotlib import pyplot as plt
from skimage.filters import threshold_local
from skimage.transform import resize
from skimage.morphology import closing, binary_closing, binary_opening
from skimage.segmentation import morphological_chan_vese, chan_vese
from skimage.feature import peak_local_max
from scipy.signal import medfilt
from scipy import ndimage as ndi
from skimage.measure import label
from celldataset import IndexTracker

# import cv2
# from matplotlib import pyplot as plt
import morphsnakes as ms

# from region_grow import regionGrowing
from skimage.feature import peak_local_max
from skimage.segmentation import watershed, random_walker, find_boundaries

# def visual_callback_3d(fig=None, plot_each=1):
# import geodesic_distance
import os
from skimage.external import tifffile

# from denseinference import CRFProcessor
from bqapi.comm import BQCommError
import h5py

#######################################################################


from scipy import ndimage
from scipy.ndimage import measurements
import SimpleITK as sitk
from skimage import segmentation
from skimage import io
import os
import pandas as pd


def adj_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = np.zeros((n, n))
    np.fill_diagonal(adj_matrix, 0)
    for i in range(1, n + 1):
        for j in adj_list[i]:
            adj_matrix[i - 1, j - 1] = 1
    return adj_matrix


def compute_cell_adjacent_table(seg_img):
    # seg_img[seg_img==17]=15
    Adjacent_table = {}
    all_labels = np.unique(seg_img)
    print(all_labels)
    # all_labels = np.delete(all_labels,all_labels==0)
    for i in all_labels:
        if i != 0:
            index_list = []
            for j in all_labels:
                if j != 0:
                    draw_board = np.zeros(seg_img.shape)
                    if i != j:
                        draw_board[seg_img == i] = 1
                        draw_board[seg_img == j] = 1
                        draw_board = ndimage.binary_dilation(draw_board).astype(
                            draw_board.dtype
                        )
                        _, num = measurements.label(draw_board)
                        if num == 1:
                            index_list.append(j)
                tmp_dict = {}
                tmp_dict[i] = index_list
                Adjacent_table.update(tmp_dict)
    return Adjacent_table


def compute_contact_points(seg_img, Adj_matrix):
    n = len(Adj_matrix)
    [slices, x, y] = seg_img.shape
    wall = np.zeros([x, y])
    for i in range(n):
        for j in range(n):
            if Adj_matrix[i, j] == 1:
                draw_board = np.zeros([slices, x, y])
                draw_contact = np.zeros([x, y])
                for k in range(slices - 1, -1, -1):
                    # fig = plt.figure()
                    draw_board1 = np.zeros([x, y])
                    draw_board2 = np.zeros([x, y])
                    draw_board1[seg_img[k] == i + 1] = 1
                    draw_board1 = ndimage.binary_dilation(draw_board1).astype(
                        draw_board1.dtype
                    )
                    draw_board2[seg_img[k] == j + 1] = 1
                    # fig.add_subplot(3,1,1)
                    # plt.imshow(draw_board1,cmap='gray')
                    # fig.add_subplot(3,1,2)
                    # plt.imshow(draw_board2,cmap='gray')
                    draw_board2 = ndimage.binary_dilation(draw_board2).astype(
                        draw_board2.dtype
                    )
                    draw_board[k, :, :] = np.logical_and(
                        draw_board1 == 1, draw_board2 == 1
                    )
                    draw_board[k, :, :] = draw_board[k, :, :] * 1
                    # filename =  "adjacent_cell_bound/{}{}slice{}.png".format(i+1,j+1,k+1)
                    # io.imsave(filename,draw_board[k,:,:])
                    # print "cell {} and cell {} in slice {}".format(i+1,j+1,k+1)
                    # fig.add_subplot(3,1,3)
                    # plt.imshow(draw_board,cmap='gray')
                    # plt.show()
                    # _,num = measurements.label(draw_board)
                    # if num==1:
                    #    wall = segmentation.find_boundaries(draw_board,connectivity=1,mode="thick")
                    #    break
                bound_len = np.zeros(slices)
                for kk in range(slices):
                    bound_len[kk] = draw_board[kk, :, :].sum()
                print(bound_len)
                for kk in range(slices - 1, 0, -1):
                    if kk < slices - 1:
                        if (
                            bound_len[kk] > bound_len[kk + 1]
                            and bound_len[kk] > bound_len[kk - 1]
                        ):
                            draw_contact_temp = draw_board[kk, :, :]
                            draw_contact = np.zeros(draw_board.shape)
                            for jj in range(len(draw_contact)):
                                draw_contact[jj] = draw_contact_temp
                            filename = "data5_contact/{}{}slice{}.nii.gz".format(
                                i + 1, j + 1, kk + 1
                            )
                            draw_contact_img = sitk.GetImageFromArray(
                                (draw_contact * 255).astype("uint8")
                            )
                            sitk.WriteImage(draw_contact_img, filename)
                            break
    return wall


def compute_conjunction_points(seg_img, Adj_list):
    #     print "compute conjunction points"
    # seg_img[seg_img==17]=15
    [slices, x, y] = seg_img.shape
    n = len(Adj_list)
    plane = seg_img[int(len(seg_img) / 2 + 1)]
    final = np.zeros((x, y))
    final_dict = {}
    for i in Adj_list.keys():
        A = i
        A_neighbors = Adj_list[A]
        for j in range(len(A_neighbors)):
            B = A_neighbors[j]
            B_neighbors = Adj_list[B]
            for k in range(len(B_neighbors)):
                C = B_neighbors[k]
                draw_board1 = np.zeros((x, y))
                draw_board2 = np.zeros((x, y))
                draw_board3 = np.zeros((x, y))
                draw_board = np.zeros((x, y))
                if C in A_neighbors:
                    draw_board1[plane == A] = 1
                    draw_board2[plane == B] = 1
                    draw_board3[plane == C] = 1
                    draw_board1 = ndimage.binary_dilation(
                        draw_board1, iterations=1
                    ).astype(draw_board1.dtype)
                    draw_board2 = ndimage.binary_dilation(
                        draw_board2, iterations=1
                    ).astype(draw_board2.dtype)
                    draw_board3 = ndimage.binary_dilation(
                        draw_board3, iterations=1
                    ).astype(draw_board3.dtype)
                    # print "cell {} {} {}".format(A,B,C)
                    # plt.imshow(draw_board1)
                    # plt.show()
                    draw_board = np.logical_and(draw_board1 == 1, draw_board2 == 1)
                    draw_board = np.logical_and(draw_board == 1, draw_board3 == 1)
                    draw_board = draw_board * 1
                    point = np.nonzero(draw_board)
                    if len(point[0]) > 0:
                        final_dict["{} {} {}".format(A, B, C)] = point
                    # final = np.logical_or(draw_board,final)
    # final = final*1
    # points = np.nonzero(final)
    return final_dict


def cell_volumn(seg_img):
    print("Compute each cell volumn")
    all_labels = np.unique(seg_img)
    cell_volumn = []
    unique, counts = np.unique(seg_img, return_counts=True)
    result = dict(zip(unique, counts))
    result.pop(0)
    return result


def cell_center(seg_img):
    results = {}
    for label in np.unique(seg_img):
        if label != 0:
            all_points_z, all_points_x, all_points_y = np.where(seg_img == label)
            avg_z = np.round(np.mean(all_points_z))
            avg_x = np.round(np.mean(all_points_x))
            avg_y = np.round(np.mean(all_points_z))
            results[label] = [avg_z, avg_x, avg_y]
    return results


def seg_img_coord(seg_img):
    coords = {}
    for label in np.unique(seg_img):
        if label != 0:
            coordinate = np.argwhere(seg_img == label)
            coords[label] = coordinate
    return coords


def slice_det(img):
    slice_ind = 0
    max_intensity = 0
    for i in range(len(img)):
        intensity = sum(sum(img[i]))
        if intensity > max_intensity:
            max_intensity = intensity
            slice_ind = i - 1
    return slice_ind


def relabel(seg_img):
    new_label = 0
    for old_label in np.unique(seg_img):
        seg_img[seg_img == old_label] = new_label
        new_label = new_label + 1
    return seg_img


######################################################################


import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw
from matplotlib import cm
from colorsys import hsv_to_rgb
import matplotlib

matplotlib.use("Agg")
random_cmap = True


class MyCMap:
    def __init__(self, n):  # Creates a 2D array of colors, size (n,3)
        self.colors = np.zeros((n, 3))
        for i in range(1, n):  # color for 0 is always black
            self.colors[i] = hsv_to_rgb(
                np.random.uniform(), 1.0, 1.0
            )  # random hues for all others

    def map(self, X):
        X_shape = X.shape
        return self.colors[X.astype(int).reshape(-1)].reshape(X.shape + (3,))


def get_means(
    l, counts
):  # helper function for get_stats (same process need for x and y)
    l_cumsums = np.hstack((0, np.cumsum(l)))[np.cumsum(counts)]
    l_sums = l_cumsums - np.hstack((0, l_cumsums[:-1]))
    return np.divide(l_sums, counts, where=(counts != 0))


def get_stats(A):  # A is an array of integer values, denoting different masks
    h, w = A.shape
    sort_inds = np.argsort(A, axis=None)
    x = np.arange(w)[
        sort_inds % w
    ]  # finds x-coordinate corresponding to nth largest value
    y = np.arange(h)[sort_inds // w]  # finds y coordinate
    counts = np.bincount(A.reshape(-1))  # creates histogram of values for integers
    boxes = np.vstack(
        (
            np.arange(counts.shape[0]),  # (mask value, x mean, y mean, #pixels)
            get_means(x, counts),
            get_means(y, counts),
            counts,
        )
    ).T
    boxes = boxes[
        boxes[:, 3] != 0
    ]  # get_means() does not remove cases where counts=0, do that here
    return boxes


def bound(x, upper):
    return max(0, min(x, upper))


def draw_text(d, text, center, font, color, img_dims):
    w, h = d.textsize(text, font=font)
    nw_corner = (
        bound(center[1] - w // 2, img_dims[1] - w),
        bound(center[0] - h // 2, img_dims[0] - h),
    )

    d.text(nw_corner, text, font=font, fill=color)


scale = 0.25
min_font = 10
darken = 0.7

n_max = None


def label_segmentation(tiff_filename):

    # Read in Tifffile
    img = tifffile.imread(tiff_filename)

    # Get number of Slices
    num_slices, h, w = img.shape
    # print("Image Shape: ", img.shape, "\nNumber of Slices: ", img.shape[0])
    cmap = MyCMap(img.max() + 1)
    labeled_image = np.empty(img.shape + (3,))
    for idx, arr in enumerate(img[:n_max]):

        boxes = get_stats(arr)
        if np.all(arr[0] == 1) and np.all(arr[-1] == 1):
            boxes = boxes[2:]
            cmap.colors[1] = (1, 1, 1)
        else:
            boxes = boxes[1:]

        if random_cmap:
            im_arr = (255 * darken * cmap.map(arr)).astype(np.uint8)
        else:
            im_arr = (255 * darken * cm.jet(arr / arr.max())[:, :, :3]).astype(np.uint8)

        im = Image.fromarray(im_arr)
        d = ImageDraw.Draw(im)
        for index, xmean, ymean, n in boxes:
            if (
                arr[int(ymean + 0.5), int(xmean + 0.5)] == index
            ):  # checks if mean is inside cell
                font_size = max(min_font, int(scale * np.sqrt(n)))
                font = ImageFont.truetype("source/Display-Bold.otf", size=font_size)
                draw_text(
                    d,
                    str(int(index)),
                    (ymean, xmean),
                    font,
                    (255, 255, 255),
                    im_arr.shape[:2],
                )
        #          else: print(f'Bad index: {index}')  #the mean is outside of cell

        labeled_image[idx] = np.array(im)

    # plt.imshow(im); plt.show()
    imMeta = "ImageJ\nimages=%d\nslices=%d\n" % (num_slices, num_slices)

    tifffile.imsave(
        tiff_filename,
        labeled_image,
        compress=1,
        metadata={"colormap": "rgb"},
        extratags=[(270, "s", 1, imMeta)],
    )
    return labeled_image


#####


def maxprojection(img):
    z, x, y = img.shape
    max_proj = np.zeros((x, y))
    max_proj = np.amax(img, axis=0)
    max_proj = max_proj.astype("float32")
    return max_proj


# def gvf(img):


def propagate(img, one_cell, sli_ind):
    z, x, y = img.shape
    sli_start, sli_end = sli_ind, sli_ind
    boundaries = find_boundaries(one_cell[sli_ind])
    # print boundaries*1
    # plt.imshow(boundaries,cmap='gray')
    # plt.show()
    one_cell[sli_ind] = boundaries * 1
    while sli_start > 0 or sli_end < z - 1:
        # print sli_start
        if sli_start > 0:
            cur = img[sli_start]
            cur_2 = one_cell[sli_start]
            points = np.transpose(np.nonzero(cur_2))
            prev_sli = np.zeros((x, y))
            for point in points:
                # print len(point)
                # print point
                prev = img[sli_start - 1]
                # print cur[point].shape
                diff = abs(
                    prev[
                        max(point[0] - 2, 0) : min(point[0] + 3, x),
                        max(point[1] - 2, 0) : min(point[1] + 3, y),
                    ]
                    - cur[point[0], point[1]]
                )
                # print diff.shape
                ind = np.unravel_index(np.argmin(diff, axis=None), diff.shape)
                prev_sli[ind[0] + point[0] - 2, ind[1] + point[1] - 2] = 1
                one_cell[sli_start - 1] = prev_sli
            sli_start = sli_start - 1
        if sli_end < z - 1:
            cur = img[sli_end]
            cur_2 = one_cell[sli_start]
            points = np.transpose(np.nonzero(cur_2))
            prev_sli = np.zeros((x, y))
            for point in points:
                prev = img[sli_start - 1]
                diff = abs(
                    prev[
                        max(point[0] - 2, 0) : min(point[0] + 3, x),
                        max(point[1] - 2, 0) : min(point[1] + 3, y),
                    ]
                    - cur[point[0], point[1]]
                )
                ind = np.unravel_index(np.argmin(diff, axis=None), diff.shape)
                prev_sli[ind[0] + point[0] - 4, ind[1] + point[1] - 4] = 1
                one_cell[sli_end + 1] = prev_sli
            sli_end = sli_end + 1
    return one_cell


def main(
    prob_map_dir, testing_data_dir, min_distance, label_threshold, black_threshold
):
    minimum = 50

    directory = prob_map_dir
    blk_threshold = 0.05
    min_dis = min_distance
    label_thresh = label_threshold
    files = os.listdir(directory)
    original_input = testing_data_dir + os.listdir(testing_data_dir)[0]
    output_files = []
    with tifffile.TiffFile(original_input) as tiff:
        imMeta = tiff.is_imagej
    for file in files:
        # print file
        blk_threshold = black_threshold

        path = os.path.join(directory, file)
        img = sitk.ReadImage(path)
        img = sitk.GetArrayFromImage(img)
        img = img.astype("float32")
        seg_new = img / np.amax(img)
        slice_ind = slice_det(seg_new)
        seg_new[seg_new < blk_threshold] = 0
        mid_slice = seg_new[slice_ind]
        mask_mid = peak_local_max(
            -mid_slice, min_distance=min_dis, indices=False, exclude_border=1
        )
        # plt.imshow(mid_slice,cmap='gray')
        # plt.show()
        mask_mid = mask_mid * 1
        mask_mid = binary_opening(1 - mask_mid)
        mask_mid = binary_closing(mask_mid)
        distance = ndi.distance_transform_edt(1 - mask_mid)
        # mask_mid = peak_local_max(distance,min_distance=30,indices=False,threshold_rel=0.2)
        mask_mid_bin = np.zeros_like(distance)
        mask_mid_bin[distance > label_thresh] = 1
        masks = label(mask_mid_bin)
        # masks_img = sitk.GetImageFromArray((masks*255).astype('uint8'))
        # sitk.WriteImage(masks_img,'/home/tom/result/'+filename+'det.png')
        uni, counts = np.unique(masks, return_counts=True)
        for i in uni:
            if counts[i] < minimum:
                masks[masks == i] = 0
        uni, counts = np.unique(masks, return_counts=True)
        mask_temp = masks
        masks = mask_temp
        # plt.imshow(masks)
        # plt.show()
        # mask = watershed(seg_new[slice_ind],masks)
        # one_cell = np.zeros_like(seg_new)
        # one_cell[slice_ind] = mask
        # masks = propagate(seg_new,one_cell,slice_ind)
        mask_3d = np.zeros_like(seg_new)
        mask_3d[slice_ind] = masks
        # last = np.zeros((512,512))
        # first = np.zeros((512,512))
        # last[400:402,259:262]=30
        # first[375:380,245:250]=1
        # mask_3d[5]=last
        # mask_3d[18*5]=last
        # mask_3d[0]=first
        # masks_img = sitk.GetImageFromArray((masks*255).astype('uint8'))
        # sitk.WriteImage(masks_img,'/home/tom/result/'+'seeds.png')
        # masks = random_walker(seg_new,mask_3d,beta=10,mode='bf')
        masks = watershed(seg_new, mask_3d, watershed_line=True)
        # CRF
        # distance_one_cell = ndi.distance_transform_edt(one_cell)
        # distance_one_cell[distance_one_cell>15] = np.amax(distance_one_cell)
        # distance_one_cell = distance_one_cell/np.amax(distance_one_cell)
        # prob_map = np.multiply(1-prob_map,one_cell)
        # pro = CRFProcessor.CRF3DProcessor()
        # seg_new = np.transpose(prob_map,(1,2,0))
        # labels = np.zeros((512,512,12,2))
        # seg_new[seg_new>0.01] = 1
        # labels[:,:,:,0] = seg_new
        # labels[:,:,:,1] = 1-seg_new
        # distance_one_cell = np.transpose(distance_one_cell,(1,2,0))
        # result = pro.set_data_and_run(seg_new,labels)
        # result = np.transpose(result,(2,0,1))
        # print np.unique(result)
        # plt.imshow(mask_mid_bin)
        # plt.show()
        # masks = resize(masks,(masks.shape[0]/5,masks.shape[1],masks.shape[2]),mode='constant')
        # masks_img = sitk.GetImageFromArray((masks).astype('uint8'))
        # file_name = os.path.splitext(file)[0]
        # outfile = os.path.join(outdir,file_name+'-seg.tif')
        # sitk.WriteImage(masks_img,outfile)
        with tifffile.TiffWriter("source/result/" + file + "seg.tif") as tif:
            for i in range(masks.shape[0]):
                tif.save(masks[i], extratags=[(270, "s", 1, imMeta)])
        labeled_image = label_segmentation("source/result/" + file + "seg.tif")

    return labeled_image


if __name__ == "__main__":
    main(
        "source/prob_map/",
        "/source/data/celldata",
        min_distance,
        label_threshold,
        black_threshold,
    )
