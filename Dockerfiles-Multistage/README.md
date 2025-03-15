# what is the need of multi-stage dockerfile?
----------------------------------------------------------------------
    #Single stage(traditional) dockerfile
    ---------------------------------------------
    Let's say we have a dockerfile. we run docker build on single stage dockerfile. It will generate a final image which will
    contains following layers.
        -----------------------------
        |      App                  |   <- must
        -----------------------------
        |     Runtime               |   <- needed as dependency to run the app
        -----------------------------
        |     SRC                   |   <- should not be part of final image
        -----------------------------
        |     Build tools           |   <- not required
        -----------------------------

    These extra layers which unneccessary increases the image size, causing resource issue. so multi-stage dockerfile fixes this issue by removing unnecessary layers which is not necessary for final image.

    what is multi-stage file?
    --------------------------
    When you see more than 1 FROM instructions in dockerfile, it is multi stage dockerfile. Basically It is used to handle image size.
    
