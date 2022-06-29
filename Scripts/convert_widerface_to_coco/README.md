## *Convert WIDERFace annotations to COCO format*

download link:http://shuoyang1213.me/WIDERFACE/

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
              
    
python scripts/convert_widerface_to_coco.py --datadir data/widerface  --subset all --outdir ./  
