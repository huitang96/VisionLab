## *Convert WIDERFace annotations to COCO format*


dataset download link:http://shuoyang1213.me/WIDERFACE/

```shell
data  
└── widerface  
    ├── wider_face_split  
    ├── WIDER_train  
    │   └── images  
    │       ├── 0--Parade  
    │       └── ...  
    └── WIDER_val  
        └── images  
            ├── 0--Parade  
            ├── ...  
```          
    
python Scripts/convert_widerface_to_coco.py --datadir data/widerface  --subset all --outdir ./  


generated: wider_face_train_annot_coco_style.json \ wider_face_val_annot_coco_style.json 
