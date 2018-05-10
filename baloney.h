char* to_str(int val){
    char outref[8];
    snprintf(outref, sizeof(outref), "%d", val);
    return outref;
}