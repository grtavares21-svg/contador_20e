import streamlit as st
import pandas as pd 
import dados
import logica 


st.set_page_config(page_title ='Contador 20€',layout='wide')

#carregar dados
guardados, historico= dados.carregar()
metricas = logica.calcular_metricas(guardados)

st.title('💶 Contador 20€ até 9000€')
st.write(f"Objetivo:**{logica.VALOR}€ x{logica.OBJETIVO}vezes**=**{metricas['objetivo_total']}€")

#Métricas

col1,col2,col3,col4 =st.columns(4)
col1.metric('Guardados',f'{guardados}/{logica.OBJETIVO}')
col2.metric('faltam',metricas['faltam'])
col3.metric('Total Guardao',f"{metricas['total_guardado']}€")
col4.metric('Progresso',f"{metricas['percent']*100:.1f}%")


st.progress(metricas['percent'])

if metricas ['faltam'] >0:
    st.info(f"Faltam**{metricas['faltam']}x20€**=**{metricas['total_falta']}€**.BORA! 🚀")
else:
    st.balloons()
    st.success("🎉 OBJETIVO BATIDO! 9000€ guardados!")

#Botões

col_btn1,col_btn2= st.columns([3,1])
with col_btn1:
    if st.button(f"✅ Guardei +{logica.VALOR}€", type="primary", use_container_width=True):
        guardados,historico = dados.adicionar_20e(guardados,historico)
        st.rerun()

with col_btn2:
    if guardados >0 and st.button("↩️ Desfazer"):
        guardados,historico = dados.desfazer(guardados,historico)
        st.rerun()
st.divider()

#Graficos
if historico:
    st.subheader("📊 Evolução Semanal")
    df=pd.DataFrame({"Data":pd.to_datetime(historico)})
    df["Semana"]=df["Data"].dt.to_period("W").astype(str) 
    grafico= df.groupby("Semana").size().reset_index(name="20€ guardados")
    st.bar_chart(grafico.set_index("Semana"))

    with st.expander("Ver histórico completo"):
        df_hist =pd.DataFrame({"#":range(1,len(historico)+1), "Data e Hora":historico})
        st.dataframe(df_hist,use_container_width=True,hide_index=True) 
          
