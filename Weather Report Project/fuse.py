
            if (cloudyAllDay2[1] + partiallyCloudyAllDay2[1])/2 > 0.8:
                videovideooutput += [v16]+[v3]+[v8] 
            elif (cloudyAllDay2[1] + partiallyCloudyAllDay2[1])/2 > 0.5:
                videooutput += [v16]+ [v10] +[v8]
            elif (cloudyAllDay2[1] + partiallyCloudyAllDay2[1])/2 > 0.0:
                videovideooutput += [v16]+[v17]+[v8]

            if (cloudyAllDay2[2] + partiallyCloudyAllDay2[2])/2 > 0.8:
                videooutput += [v16] + [v3] + [v7]
            elif (cloudyAllDay2[2] + partiallyCloudyAllDay2[2])/2 > 0.5:
                videooutput += [v16] + [v10] +[v7]
            elif (cloudyAllDay2[2] + partiallyCloudyAllDay2[2])/2 > 0.0:
                videooutput += [v16] + some [v3] + [v7]
            
            if (cloudyAllDay2[3] + partiallyCloudyAllDay2[3])/2 > 0.8:
                videooutput += [v16] + [v3] + [v5]
            elif (cloudyAllDay2[3] + partiallyCloudyAllDay2[3])/2 > 0.5:
                videooutput += [v16] + [v10] +[v5]
            elif (cloudyAllDay2[3] + partiallyCloudyAllDay2[3])/2 > 0.0:
                videooutput += [v16] + some [v3] + [v5]

            if (cloudyAllDay2[4] + partiallyCloudyAllDay2[4])/2 > 0.8:
                videooutput += [v16] + [v3] + [v6]
            elif (cloudyAllDay2[4] + partiallyCloudyAllDay2[4])/2 > 0.5:
                videooutput += [v16] + [v10] +[v6]
            elif (cloudyAllDay2[4] + partiallyCloudyAllDay2[4])/2 > 0.0:
                videooutput += [v16] + some [v3] + [v6]

            #partly cloudy erstmal ausgelassen


            if rainallDay2[1] > 0.8:
                videooutput += [v16] +[12] +  [v8]
            elif rainallDay2[1] > 0.5:
                videooutput += [v16] +[11] +  [v8]
            elif rainallDay2[1] > 0.0:
                videooutput += [v16] +[14] +  [v8]

            if rainallDay2[2] > 0.8:
                videooutput += [v16] +[12] +  [v7]
            elif rainallDay2[2] > 0.5:
                videooutput += [v16] +[11] +  [v7]
            elif rainallDay2[2] > 0.0:
                videooutput += [v16] +[14] +  [v7]
            
            if rainallDay2[3] > 0.8:
                videooutput += [v16] +[12] +  [v5]
            elif rainallDay2[3] > 0.5:
                videooutput += [v16] +[11] +  [v5]
            elif rainallDay2[3] > 0.0:
                videooutput += [v16] +[14] +  [v5]

            if rainallDay2[4] > 0.8:
                videooutput += [v16] +[12] +  [v6]
            elif rainallDay2[4] > 0.5:
                videooutput += [v16] +[11] +  [v6]
            elif rainallDay2[4] > 0.0:
                videooutput += [v16] +[14] +  [v6]
            '''
            if fogAllDay2[1] > 0.8:
                videooutput += [v16] +foggy [v8]
            elif fogAllDay2[1] > 0.5:
                videooutput += [v16] +partly foggy [v8]
            elif fogAllDay2[1] > 0.0:
                videooutput += [v16] +some foggy [v8]

            if fogAllDay2[2] > 0.8:
                videooutput += [v16] +foggy [v7]
            elif fogAllDay2[2] > 0.5:
                videooutput += [v16] +partly foggy [v7]
            elif fogAllDay2[2] > 0.0:
                videooutput += [v16] +some foggy [v7]
            
            if fogAllDay2[3] > 0.8:
                videooutput += [v16] +foggy [v5]
            elif fogAllDay2[3] > 0.5:
                videooutput += [v16] +partly foggy [v5]
            elif fogAllDay2[3] > 0.0:
                videooutput += [v16] +some foggy [v5]

            if fogAllDay2[4] > 0.8:
                videooutput += [v16] +foggy [v6]
            elif fogAllDay2[4] > 0.5:
                videooutput += [v16] +partly foggy [v6]
            elif fogAllDay2[4] > 0.0:
                videooutput += [v16] +some foggy [v6]


            
            if snowAllDay2[1] > 0.8:
                videooutput += [v16] +snowy [v8]
            elif snowAllDay2[1] > 0.5:
                videooutput += [v16] +partly snowy [v8]
            elif snowAllDay2[1] > 0.0:
                videooutput += [v16] +some snowy [v8]

            if snowAllDay2[2] > 0.8:
                videooutput += [v16] +snowy [v7]
            elif snowAllDay2[2] > 0.5:
                videooutput += [v16] +partly snowy [v7]
            elif snowAllDay2[2] > 0.0:
                videooutput += [v16] +some snowy [v7]
            
            if snowAllDay2[3] > 0.8:
                videooutput += [v16] +snowy [v5]
            elif snowAllDay2[3] > 0.5:
                videooutput += [v16] +partly snowy [v5]
            elif snowAllDay2[3] > 0.0:
                videooutput += [v16] +some snowy [v5]

            if snowAllDay2[4] > 0.8:
                videooutput += [v16] +snowy [v6]
            elif snowAllDay2[4] > 0.5:
                videooutput += [v16] +partly snowy [v6]
            elif snowAllDay2[4] > 0.0:
                videooutput += [v16] +some snowy [v6]
            '''
            if clearAllDay2[1] > 0.8:
                videooutput += [v16] +[v2] + [v8]
            elif clearAllDay2[1] > 0.5:
                videooutput += [v16] +[v9] + [v8]
            elif clearAllDay2[1] > 0.0:
                videooutput += [v16] +[v13] + [v8]

            if clearAllDay2[2] > 0.8:
                videooutput += [v16] +[v2] + [v7]
            elif clearAllDay2[2] > 0.5:
                videooutput += [v16] +[v9] + [v7]
            elif clearAllDay2[2] > 0.0:
                videooutput += [v16] +[v13] + [v7]
            
            if clearAllDay2[3] > 0.8:
                videooutput += [v16] +[v2] + [v5]
            elif clearAllDay2[3] > 0.5:
                videooutput += [v16] +[v9] + [v5]
            elif clearAllDay2[3] > 0.0:
                videooutput += [v16] +[v13] + [v5]

            if clearAllDay2[4] > 0.8:
                videooutput += [v16] +[v2] + [v6]
            elif clearAllDay2[4] > 0.5:
                videooutput += [v16] +[v9] + [v6]
            elif clearAllDay2[4] > 0.0:
                videooutput += [v16] +[v13] + [v6]