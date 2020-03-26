package com.example.myapplication;

import android.content.Context;
import android.media.MediaPlayer;

public class PlaySound {
    public static void play(String name){

        Context context = MainActivity.getcontext();
        int file_id = context.getResources().getIdentifier(name, "raw", context.getPackageName());
        if (file_id != 0){
            final MediaPlayer sound = MediaPlayer.create(context, file_id);
            sound.start();
        }
    }
}
